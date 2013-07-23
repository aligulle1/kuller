#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -R hsqldb:hsqldb /var/lib/hsqldb")
    os.system("/usr/bin/chmod -R 0750 /var/lib/hsqldb")
    os.system("/usr/bin/chmod 600 /var/lib/hsqldb/sqltool.rc")

    os.system("/usr/bin/chown -R hsqldb:hsqldb /var/log/hsqldb")
    os.system("/usr/bin/chmod 0750 /var/log/hsqldb")
    os.system("/usr/bin/chmod -R 0660 /var/log/hsqldb/*")

    os.system("/usr/bin/chown hsqldb:hsqldb /var/run/hsqldb")
    os.system("/usr/bin/chmod 0755 /var/run/hsqldb")
