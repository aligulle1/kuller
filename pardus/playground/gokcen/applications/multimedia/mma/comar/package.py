#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    # updating mma database file
    os.system("/usr/bin/mma -G")

    # chmod a+w - as specified in cp-install script of mma
    os.chmod("/usr/share/mma/lib/stdlib/.mmaDB", 0666)
