#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="framework-%s" % get.srcVERSION()

def install():
    for directory in ["data","lib","modules","plugins","scripts"]:
        pisitools.insinto("/usr/lib/metasploit",directory)

    for executable in ["msfcli","msfconsole","msfd", "msfencode","msfopcode","msfpayload","msfpescan","msfweb"]:
        pisitools.insinto("/usr/lib/metasploit",executable)

    for executable in shelltools.ls("msf*"):
        pisitools.dosym("/usr/bin/metasploit", "/usr/bin/%s" % executable)

    # Cleanup crap
    pisitools.removeDir("/usr/lib/metasploit/data/meterpreter")
    pisitools.removeDir("/usr/lib/metasploit/data/msfgui")
    pisitools.removeDir("/usr/lib/metasploit/data/templates")
    pisitools.remove("/usr/bin/msfgui")

    # .exe, .dll and .svn crap
    for root, dirs, files in os.walk(get.installDIR()):
        for name in dirs:
            if name == ".svn":
                shelltools.unlinkDir(os.path.join(root, name))
        for name in files:
            if name.endswith(".dll") or name.endswith(".exe"):
                shelltools.unlink(os.path.join(root, name))

    # msfweb disabled until Rails is packaged
    pisitools.remove("/usr/bin/msfweb")
    pisitools.remove("/usr/lib/metasploit/msfweb")
    pisitools.removeDir("/usr/lib/metasploit/data/msfweb")

    pisitools.dodoc("documentation/*.txt","documentation/*.pdf","documentation/ChangeLog","documentation/COPYING")
