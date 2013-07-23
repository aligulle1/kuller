#!/usr/bin/python

import os

def postInstall():
    # for upgrading 3.4.5 to 3.4.6
    os.system("OLDVER=\"3.4.5\" /usr/bin/gawk -f /usr/libexec/awk/fixlafiles.awk 3.4.6")
