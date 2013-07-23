#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/update-opengl ati")
