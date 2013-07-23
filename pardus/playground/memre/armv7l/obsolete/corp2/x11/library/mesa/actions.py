# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Mesa-%s" % get.srcVERSION().replace("_", "-")

def setup():
    autotools.environment["CFLAGS"] = "%(CFLAGS)s -DNDEBUG" % autotools.environment

    shelltools.sym("../../../../gallium/drivers/nouveau/nouveau_class.h", "src/mesa/drivers/dri/nouveau/nouveau_class.h")

    autotools.autoreconf("-vif")
    autotools.configure("--enable-pic \
                         --disable-xcb \
                         --disable-glx-tls \
                         --disable-gl-osmesa \
                         --disable-egl \
                         --disable-glw \
                         --disable-glut \
                         --disable-gallium \
                         --disable-gallium-nouveau \
                         --with-driver=dri \
                         --without-demos \
                         --with-dri-driverdir=/usr/lib/xorg/modules/dri \
                         --with-dri-drivers=swrast \
                         --with-state-trackers=dri,glx")

    pisitools.dosed("src/mesa/shader/slang/library/Makefile", r"(^GLSL_CL\s*=).*", "\\1 $(TOP)/glsl-compile")

def build():
    # building host-side tool(s)
    if not shelltools.can_access_file("glsl-compile"):
        for q in [ "pp", "cl", "apps" ]:
            autotools.environment["q"] = q
            autotools.make('-C src/glsl/%(q)s -j1 \
                            CC="%(HOSTCC)s" \
                            APP_CC="%(HOSTCC)s" \
                            CFLAGS="%(HOSTCFLAGS)s" \
                            HOST_CC="%(HOSTCC)s" \
                            HOST_CFLAGS="%(HOSTCFLAGS)s"' % autotools.environment)
            if q == "apps":
                shelltools.system("mv {src/glsl/apps/,glsl-}compile")

        # cleaning host-side-compiled libs and apps in order to compile them for target
        for q in [ "pp", "cl", "apps" ]:
            autotools.environment["q"] = q
            autotools.make('-C src/glsl/%(q)s clean' % autotools.environment)

    autotools.make()

    # Build glxinfo/gears
    autotools.make('-C progs/xdemos glxinfo glxgears')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fatih didnt want it.
    #xdemos = ("corender",  "glsync",         "glthreads",           "glxcontexts",
              #"glxdemo",   "glxgears",       "glxgears_fbconfig",   "glxgears_pixmap",
              #"glxheads",  "glxinfo",        "glxpbdemo",           "glxpixmap",
              #"glxsnoop",  "glxswapcontrol", "manywin",             "multictx",
              #"offset",    "overlay",        "pbdemo",              "pbinfo",
              #"sharedtex", "sharedtex_mt",   "texture_from_pixmap", "wincopy",
              #"xfont",     "xrotfontdemo")

    #for xdemo in xdemos:
        #pisitools.dobin("progs/xdemos/%s" % xdemo)

    pisitools.dobin("progs/xdemos/glxinfo")
    pisitools.dobin("progs/xdemos/glxgears")

    # Don't install unused headers
    #for header in ("[a-fh-wyz]*.h", "gg*.h", "glf*.h", "*glut*.h"):
    for header in ("[a-fh-wyz]*.h", "glf*.h"):
        pisitools.remove("/usr/include/GL/%s" % header)

    ## Moving libGL for dynamic switching
    #pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/mesa")

    pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")
