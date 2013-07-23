#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/pisi/package"):
        os.system("mkdir /var/lib/pisi/package")
        os.system("mv /var/lib/pisi/* /var/lib/pisi/package/")
        os.system("mv /var/lib/pisi/package/scripts /var/lib/pisi/")

    if os.path.exists("/var/lib/pisi/index"):
        # Migrate possible x86-64.comu.edu.tr repos to the new ones
        os.system(r"sed -i 's:x86-64.comu.edu.tr:packages.pardus.org.tr/pardus/corporate2/stable/x86_64:' /var/lib/pisi/index/*/uri")

        # Use the new .xz indexes by default
        os.system(r"sed -i 's:\.bz2$:.xz:' /var/lib/pisi/index/*/uri")
