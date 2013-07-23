# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown zeroinst:zeroinst /var/cache/0install.net/implementations")
