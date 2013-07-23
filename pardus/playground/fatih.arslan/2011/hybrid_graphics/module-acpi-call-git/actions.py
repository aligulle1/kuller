#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()

WorkDir = "git-dummy-package"
gitroot = "http://github.com/mkottman/acpi_call.git"
gitname = "acpi_call"
gitbuild = gitname + "-build"

def setup():
    # Don't clone it over and over again
    if shelltools.can_access_directory(gitname):
        shelltools.cd(gitname)
        shelltools.system("git pull origin")
        shelltools.cd("..")
    else:
        shelltools.system("git clone %s" % gitroot)

    # Create seperate build dir. Don't mess up with original git repo
    if shelltools.can_access_directory(gitbuild):
        shelltools.unlinkDir(gitbuild)
    shelltools.copytree(gitname, gitbuild)

def build():
    shelltools.cd(gitbuild)
    autotools.make()

def install():
    shelltools.cd(gitbuild)

    # Userspace tools
    pisitools.dobin("asus1215n.sh")
    pisitools.dobin("m11xr2.sh")
    pisitools.dobin("test_off.sh")

    pisitools.insinto("/usr/share/%s/" % gitname, "query_dsdt.pl")
    pisitools.insinto("/usr/share/%s/" % gitname, "windump_hack")

    # Our lovely kernel module
    pisitools.insinto("/lib/modules/%s/kernel/drivers/acpi/" % KDIR, "acpi_call.ko")

    pisitools.dodoc("README")

