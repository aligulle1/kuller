#!/usr/bin/python

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    PACKAGE = "kernel-debug"
    SUFFIX = "debug"
    import os.path
    if os.path.exists("/boot/grub/grub.conf"):
        if SUFFIX:
            version = "%s-%s-%s" % (toVersion, toRelease, SUFFIX)
        else:
            version = "%s-%s" % (toVersion, toRelease)
        call("grub", "Boot.Loader", "updateKernelEntry", (version, ""))

def preRemove():
    pass
