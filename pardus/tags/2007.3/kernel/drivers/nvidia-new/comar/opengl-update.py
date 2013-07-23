#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/update-opengl nvidia")

def preRemove():
    os.system("/sbin/update-opengl xorg-x11")
