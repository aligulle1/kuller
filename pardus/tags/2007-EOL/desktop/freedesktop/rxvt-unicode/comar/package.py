#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    os.system("/usr/bin/tic /usr/share/terminfo/r/rxvt-unicode")
