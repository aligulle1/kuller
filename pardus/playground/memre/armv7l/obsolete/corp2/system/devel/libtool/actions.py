#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libtool-%sb" % get.srcVERSION()
configTemplateDir = "/usr/share/libtool/config"

# FIXME: do we still need this ?
pathFixList = {"libpath1": ["sys_lib_search_path_spec=.*", "sys_lib_search_path_spec=\"/lib /usr/lib /usr/local/lib\""],
               "libpath2": ["sys_lib_dlsearch_path_spec=.*", "sys_lib_dlsearch_path_spec=\"/lib /usr/lib /usr/local/lib\""],
               "gccpath1": ["predep_objects=.*", "predep_objects=\"\""],
               "gccpath2": ["postdep_objects=.*", "postdep_objects=\"\""],
               "gccpath3": ["compiler_lib_search_path=.*", "compiler_lib_search_path=\"\""]}

def setup():
    crosstools.environment["CFLAGS"] = "%s -fPIC" % crosstools.environment["CFLAGS"]

    crosstools.configure("--enable-static=no")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/bin/%(target)s-libtool" % crosstools.environment, "libtool")

    for f in ["config.sub", "config.guess"]:
        pisitools.remove("%s/%s" % (configTemplateDir, f))
        pisitools.dosym("/usr/share/gnuconfig/%s" % f, "%s/%s" % (configTemplateDir, f))

    # Fix default lib paths and don't let gcc paths sneak in
    for i in pathFixList.keys():
        pisitools.dosed("%s/usr/bin/libtool" % get.installDIR(), pathFixList[i][0], pathFixList[i][1])

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "THANKS", "doc/PLATFORMS")
