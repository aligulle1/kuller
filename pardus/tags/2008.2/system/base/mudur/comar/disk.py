#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import subprocess

FSTAB = '/etc/fstab'

class DMException(Exception):
    pass

def parseFstab(fstab):
    if not os.access(fstab, os.R_OK):
        raise DMException, 'Unable to read "%s"' % fstab
    entries = []
    for line in open(fstab):
        line = line.strip()
        if line.startswith('#'):
            continue
        entries.append(line.replace('\t', ' ').split())
    return entries

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
            parts.append(line.split()[0])
    return parts

def mount(device, path):
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
    if device in listEntries():
        removeEntry(device)
    _options = []
    for key, value in options.iteritems():
        if value:
            _options.append('%s=%s' % (key, value))
        else:
            _options.append(key)
    if file(FSTAB).read()[-1] != '\n':
        file(FSTAB, 'a').write('\n')
    file(FSTAB, 'a').write('%s %s %s %s 0 0\n' % (device, path, fsType, ','.join(_options)))

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
    raise DMException, 'Device not found in entry list'

def removeEntry(device):
    if device not in listEntries():
        raise DMException, 'Device not found in entry list'
    newlines = []
    for line in open(FSTAB):
        line = line.strip()
        if line.replace('\t', ' ').split()[0] != device:
            newlines.append(line)
    file(FSTAB, 'w').write('\n'.join(newlines))
