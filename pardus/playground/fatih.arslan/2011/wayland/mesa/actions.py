# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "Mesa-%s" % get.srcVERSION().replace("_", "-")
WorkDir = "mesa-7.11"

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    shelltools.system("./autogen.sh")

    autotools.autoreconf("-vif")

    # gallium-lvm is enabled by default by commit a86fc719d6402eb482657707741890e69e81700f
    options ="--enable-pic \
              --disable-xcb \
              --enable-glx-tls \
              --disable-gl-osmesa \
              --enable-egl \
              --enable-gles2 \
              --disable-glw \
              --disable-glut \
              --enable-gallium-llvm \
              --disable-gallium-egl \
              --enable-shared-glapi \
              --with-gallium-drivers=i915,i965,nouveau,r300,r600,svga,swrast \
              --with-driver=dri \
              --with-egl-platforms=x11,wayland,drm \
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-dri-drivers=i810,i915,i965,mach64,nouveau,r128,r200,r600,radeon,sis,tdfx"


    if get.buildTYPE() == "emul32":
        # compile with llvm doesn't work for now, test it later
        options += " --libdir=/usr/lib32 \
                     --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                     --disable-gallium-llvm \
                     --enable-32-bit"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)

    pisitools.dosed("configs/autoconf", "(PYTHON_FLAGS) = .*", r"\1 = -t")

def build():
    autotools.make("-C src/glsl glsl_lexer.cpp")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.rename("/usr/lib32/xorg/modules/dri/swrastg_dri.so", "swrast_dri.so")
        return

    # Use llvmpipe instead of classic swrast driver
    pisitools.rename("/usr/lib/xorg/modules/dri/swrastg_dri.so", "swrast_dri.so")

    # Don't install unused headers
    #for header in ("[a-fh-wyz]*.h", "glf*.h"):
    for header in ("[a-fh-wyz]*.h", "glf*.h", "*glut*.h"):
        pisitools.remove("/usr/include/GL/%s" % header)

    # Moving libGL for dynamic switching
    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/mesa")

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
