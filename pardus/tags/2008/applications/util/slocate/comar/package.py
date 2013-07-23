#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R root:slocate /var/lib/slocate")
    os.system("/bin/chmod 0750 /var/lib/slocate")

    os.system("/bin/chmod 0755 /etc/cron.daily/slocate")

    os.system("/bin/chown root:slocate /usr/bin/slocate")
    os.system("/bin/chmod go-r,g+s /usr/bin/slocate")
