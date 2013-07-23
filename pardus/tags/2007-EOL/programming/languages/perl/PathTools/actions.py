#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("MANIFEST", "ChangeLog")

    # Fix file conflicts
    pisitools.remove("/usr/share/man/man3/File::Spec::Win32.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::Mac.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::VMS.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::Epoc.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::Functions.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::OS2.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::Cygwin.3pm")
    pisitools.remove("/usr/share/man/man3/Cwd.3pm")
    pisitools.remove("/usr/share/man/man3/File::Spec::Unix.3pm")
