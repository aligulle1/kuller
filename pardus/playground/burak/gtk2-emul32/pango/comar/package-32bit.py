#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    modulepath = "/etc/pango/32bit"

    if not os.path.exists(modulepath):
        os.makedirs(modulepath, 0755)
    f = open("%s/pango.modules" % modulepath, "w")
    p = os.popen("/usr/bin/pango-querymodules-32bit", "r")
    f.writelines(p.readlines())
    f.close()
    p.close()
