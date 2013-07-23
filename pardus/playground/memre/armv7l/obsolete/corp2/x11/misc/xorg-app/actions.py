# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
SkipList = (".", "filelist", "patches", "pisiBuildState")

def setup():
    # Speed up xkbcomp
    autotools.environment["CFLAGS"] = "%(CFLAGS)s -DHAVE_STRCASECMP" % autotools.environment

    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        print "Configuring %s..." % package
        shelltools.cd(package)

        if package.startswith("xsm") or not shelltools.isFile("configure"):
            autotools.autoreconf("-vif")

        cache = [ "ac_cv_file__etc_X11_fontpath_d=yes",
                  "ac_cv_file__etc_man_conf=yes",
                  "ac_cv_func_malloc_0_nonnull=yes",
                  "ac_cv_func_calloc_0_nonnull=yes",
                  "ac_cv_func_realloc_0_nonnull=yes" ]

        args = "--disable-dependency-tracking \
                --disable-devel-docs \
                --with-cpp=/usr/bin/mcpp"

        if package.startswith('xfs'):
            args += " --with-default-font-path=/etc/X11/fontpath.d"

        autotools.configure("%s" % args, cache=cache)
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
