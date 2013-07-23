#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chmod 722 /home/ftp/incoming")
    os.system("/usr/bin/chown ftp:ftp /home/ftp/incoming -R")
