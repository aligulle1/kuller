#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for lib in ("libnimMockNodes",
                "libnimCodecs",
                "libnimRecorder"):
        os.system("/usr/bin/niReg -r /usr/lib/%s.so" % lib)

def preRemove():
    for lib in ("libnimMockNodes",
                "libnimCodecs",
                "libnimRecorder"):
        os.system("/usr/bin/niReg -u /usr/lib/%s.so" % lib)
