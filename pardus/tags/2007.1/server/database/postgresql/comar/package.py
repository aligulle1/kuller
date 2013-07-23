#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown -R postgres:postgres /var/lib/postgresql")
    os.system("/usr/bin/chmod -R 0700 /var/lib/postgresql/data")
    os.system("/usr/bin/chmod -R 0700 /var/lib/postgresql/backups")

    # On first install...
    if not os.access("/var/lib/postgresql/data/base", os.F_OK):
        os.system("/usr/bin/sudo -u postgres /usr/bin/initdb --pgdata /var/lib/postgresql/data")

