#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "smolt-%s" % get.srcVERSION()

SmoonDir = "/usr/share/smoon"
ConfigDir = "/etc/smoon"

def install():
    # Do not use setup.py, mmcgrath suggested to copy whole tree.
    shelltools.copytree("%s/smolt-%s/smoon" % (get.workDIR(), get.srcVERSION()), "%s/%s" % (get.installDIR(), SmoonDir))

    # Myth support is not ready. I don't know what myth is anyway...
    pisitools.removeDir("%s/db" % SmoonDir)
    pisitools.removeDir("%s/db_myth" % SmoonDir)

    pisitools.dosym("%s/start-hardware.py" % SmoonDir, "/usr/bin/start-hardware")

    # Move config files under etc.
    pisitools.domove("%s/dev.cfg" % SmoonDir, "%s/" % ConfigDir)
    pisitools.domove("%s/hardware/config/app.cfg" % SmoonDir, "%s/" % ConfigDir)
    pisitools.domove("%s/hardware/config/log.cfg" % SmoonDir, "%s/" % ConfigDir)

    # Smoon look at configs in hardware/config.
    pisitools.dosym("%s/dev.cfg" % ConfigDir, "%s/hardware/config/dev.cfg" % SmoonDir)
    pisitools.dosym("%s/app.cfg" % ConfigDir, "%s/hardware/config/app.cfg" % SmoonDir)
    pisitools.dosym("%s/log.cfg" % ConfigDir, "%s/hardware/config/log.cfg" % SmoonDir)
