#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # /usr/kde/4/bin/pykdeuic4 is symlink to this
    os.chmod("/usr/kde/4/share/apps/pykde4/pykdeuic4.py", 0755)
