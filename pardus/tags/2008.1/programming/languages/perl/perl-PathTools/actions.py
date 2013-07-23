#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (C) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("MANIFEST", "Changes")

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
