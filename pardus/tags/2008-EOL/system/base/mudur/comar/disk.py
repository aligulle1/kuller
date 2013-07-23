#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import subprocess

FSTAB = '/etc/fstab'

FAIL_FSTAB = {
    "en": "Unable to read '%s'.",
    "tr": "'%s' okunamadı.",
}

FAIL_PATH = {
    "en": "'%s' is not a valid mount point.",
    "tr": "'%s' geçerli bir bağlama noktası değil.",
}

FAIL_ENTRY = {
    "en": "Device '%s' not found in entry list.",
    "tr": "'%s' aygıtı listede bulunamadı.",
}

class DMException(Exception):
    pass

def parseFstab(fstab):
    if not os.access(fstab, os.R_OK):
        raise DMException, _(FAIL_FSTAB) % fstab
    entries = []
    for line in open(fstab):
        line = line.strip()
        if line.startswith('#'):
            continue
        entries.append(line.replace('\t', ' ').split())
    return entries

def createPath(device, path):
    real_path = path
    if not os.path.exists(path) and os.path.exists(os.path.dirname(path)):
        # Mount point does not exist, but parent directory does.
        path = os.path.dirname(path)
        if not os.path.ismount(path) and not os.path.islink(path) and os.path.isdir(path):
            os.mkdir(real_path, 0755)
            return True
    else:
        if os.path.ismount(path):
            # Path is already mounted, allow user to use that mount point if it's already mounted
            for _device, _path in getMounted():
                if device == _device and _path == path:
                    return True
        else:
            if not os.path.islink(path) and os.path.isdir(path) and os.listdir(path) == []:
                return True
    return False

# Disk.Manager methods

def getDevices():
    from pardus.diskutils import EDD
    return EDD().blockDevices()

def getDeviceByLabel(label):
    root = '/dev/disk/by-label'
    path = os.path.join(root, label)
    if os.access(path, os.R_OK):
        return os.path.realpath(os.path.join(root, os.readlink(path)))
    else:
        return ''

def getDeviceParts(device):
    if not os.path.exists(device):
        return []
    return [x for x in glob.glob("%s*" % device) if x != device]

def getMounted():
    parts = []
    for line in open('/proc/mounts'):
        if line.startswith('/dev/'):
            device, path, other = line.split(" ", 2)
            parts.append((device, path, ))
    return parts

def mount(device, path):
    if device.startswith("LABEL="):
        device = getDeviceByLabel(device.split("LABEL=")[1])
    subprocess.call(['/bin/mount', device, path])

def umount(device):
    subprocess.call(['/bin/umount', device])

def listEntries():
    try:
        devices = [x[0] for x in parseFstab(FSTAB)]
        return devices
    except DMException:
        return []

def addEntry(device, path, fsType, options):
    path_own = False
    if device in listEntries():
        old_path, old_fsType, old_options = getEntry(device)
        # Who has that mount point? me?
        if old_path == path:
            path_own = True
        # Remove previous one to prevent duplicates
        removeEntry(device)
    if not path_own:
        if not createPath(device, path):
            fail(_(FAIL_PATH) % path)
    _options = []
    for key, value in options.iteritems():
        if value:
            _options.append('%s=%s' % (key, value))
        else:
            _options.append(key)
    if file(FSTAB).read()[-1] != '\n':
        file(FSTAB, 'a').write('\n')
    file(FSTAB, 'a').write('%s %s %s %s 0 0\n' % (device, path, fsType, ','.join(_options)))
    # Notify clients
    notify("Disk.Manager", "changed", ())
    # Mount device
    mount(device, path)

def getEntry(device):
    entries = parseFstab(FSTAB)
    for entry in entries:
        if entry[0] == device:
            _path, _fsType, _options, _dump, _pass = entry[1:]
            options = {}
            for part in _options.split(','):
                if "=" in part:
                    key, value = part.split('=', 1)
                    options[key] = value
                else:
                    options[part] = ""
            return _path, _fsType, options
    fail(_(FAIL_ENTRY) % device)

def removeEntry(device):
    if device not in listEntries():
        fail(_(FAIL_ENTRY) % device)
    newlines = []
    for line in open(FSTAB):
        line = line.strip()
        if line.replace('\t', ' ').split()[0] != device:
            newlines.append(line)
    file(FSTAB, 'w').write('\n'.join(newlines))
    if file(FSTAB).read()[-1] != '\n':
        file(FSTAB, 'a').write('\n')
    # Notify clients
    notify("Disk.Manager", "changed", ())
