#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/hcfpciconfig --serial --region=AUTO --auto")
