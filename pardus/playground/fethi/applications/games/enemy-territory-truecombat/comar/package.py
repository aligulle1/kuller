#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 777 -R /opt/enemy-territory/tcetest")
