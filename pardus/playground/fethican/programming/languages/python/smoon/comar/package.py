#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import dircache

def preRemove():
    list = dircache.listdir("/usr/share/smoon/hardware/static/stats")
    for file in list:
        os.remove("/usr/share/smoon/hardware/static/stats/%s" % file)

    os.rmdir("usr/share/smoon/hardware/static/stats")
