#!/usr/bin/python

import os

kernelVersionDir = "/etc/kernel"
initramfsConfFile = "/etc/initramfs.conf"
grubConf = "/boot/grub/grub.conf"

def loadFile(_file):
    try:
        f = file(_file)
        d = [a.lstrip().rstrip("\n") for a in f]
        f.close()
        return d
    except:
        print "mkinitramfs post: could not read %s" % _file
        return []

def writeFile(_file, data):
    try:
        f = open(_file, "w")
        f.write(data)
        f.close()
    except:
        print "mkinitramfs post: could not write to %s" % _file

def getKernelVersions():
    kl = []
    try:
        for i in os.listdir(kernelVersionDir):
            kv = open("%s/%s" % (kernelVersionDir, i)).read()
            kl.append("kernel-%s" % kv)
    except OSError:
        print "mkinitramfs post: could not get kernel versions"

    return kl

def getDevices():
    rootdev = ""
    resumedev = ""
    data = ""

    if os.path.exists(initramfsConfFile):
        icf = loadFile(initramfsConfFile)
        changed = False

        for line in icf:
            print line
            if line.startswith("root="):
                rootdev = line
                changed = True
            elif line.startswith("resume="):
                resumedev = line
                changed = True
            else:
                data += "%s\n" % line

        if changed:
            if data == "":
                os.unlink(initramfsConfFile)
            else:
                writeFile(initramfsConfFile, data)

    return rootdev, resumedev

def updateGrubConf(kv, rootdev, resumedev):
    grubdata = loadFile(grubConf)
    data = ""

    for line in grubdata:
        found = False
        if not line.startswith("#") and not " root=" in line:
            for i in kv:
                # keep the space, it is important
                kernelline = "/boot/%s " % i
                if kernelline in line:
                    data += "%s %s %s\n" % (line, rootdev, resumedev)
                    found = True

        if not found:
            data += "%s\n" % line

    writeFile(grubConf, data)


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.path.exists(initramfsConfFile):
        # write root= to grub.conf since it is used by suspend to disk

        kernelVersions = getKernelVersions()
        rootDevice, resumeDevice = getDevices()

        if len(kernelVersions) > 0 and rootDevice != "":
            updateGrubConf(kernelVersions, rootDevice, resumeDevice)



