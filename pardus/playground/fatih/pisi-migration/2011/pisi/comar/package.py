#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/pisi/package"):
        os.system("mkdir /var/lib/pisi/package")
        os.system("mv /var/lib/pisi/* /var/lib/pisi/package/")
        os.system("mv /var/lib/pisi/package/scripts /var/lib/pisi/")

    if os.path.exists("/var/lib/pisi/index"):
        os.system(r"sed -i 's:\.bz2$:.xz:' /var/lib/pisi/index/*/uri")
