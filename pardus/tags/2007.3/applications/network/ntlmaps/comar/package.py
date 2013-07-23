#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown ntlmaps:ntlmaps /etc/ntlmaps/server.cfg")
    os.system("/usr/bin/mkdir -m 0770 /var/log/ntlmaps")
    os.system("/usr/bin/chown ntlmaps:ntlmaps /var/log/ntlmaps")
