#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/hsfconfig --serial --region=AUTO --auto")
