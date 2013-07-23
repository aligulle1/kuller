#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.dodir("/usr/lib/autopsy")
    pisitools.insinto("/usr/lib/autopsy", "base/autopsy.base", "autopsy")
    pisitools.dosed("lib/Main.pm", "conf.pl", "/etc/autopsy.pl")
    shelltools.chmod("%s/usr/lib/autopsy/autopsy" % get.installDIR(), 0755)
    pisitools.insinto("/usr/lib/autopsy", "lib/")
    pisitools.insinto("/usr/lib/autopsy", "help/")
    pisitools.insinto("/usr/lib/autopsy", "pict/")
    pisitools.dodoc("CHANGES.txt", "README.txt", "TODO.txt", "docs/sleuthkit-informer-13.txt")
    pisitools.doman("man/man1/autopsy.1")
    pisitools.dosym("/usr/lib/autopsy/autopsy", "/usr/bin/autopsy")
