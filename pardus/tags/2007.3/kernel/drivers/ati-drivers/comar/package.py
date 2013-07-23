#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/update-opengl ati")

def preRemove():
    os.system("/sbin/update-opengl xorg-x11")
