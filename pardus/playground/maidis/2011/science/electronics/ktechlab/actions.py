#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
gitroot = "git://ktechlab.git.sourceforge.net/gitroot/ktechlab/ktl-zoltan_p"
gitname = "ktl-zoltan_p"
gitbuild = gitname + "-build"

shelltools.export("HOME", get.workDIR())


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

    shelltools.cd(gitbuild)
    cmaketools.configure()

def build():
    shelltools.cd(gitbuild)
    cmaketools.make()

def install():
    shelltools.cd(gitbuild)
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
