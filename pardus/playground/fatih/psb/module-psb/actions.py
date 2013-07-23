# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "psb-kernel-source-%s" % get.srcVERSION()
KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("LINUXDIR=/lib/modules/%s/build DRM_MODULES=psb" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*.ko")

    for header in ("psb_drm.h", "psb_reg.h"):
        pisitools.insinto("/usr/include/psb/drm", header)
