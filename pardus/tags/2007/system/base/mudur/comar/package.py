#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def postInstall():
    # add disks into fstsb
    os.system("/sbin/update-fstab")
