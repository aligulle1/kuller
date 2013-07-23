#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import cmaketools

WorkDir = "luatex-beta-%s" % get.srcVERSION()
GetWorkdir = "%s/%s" % (get.workDIR(), WorkDir)

def exportEnv():
    shelltools.export("AR","/usr/bin/ar")
    shelltools.export("RANLIB","/usr/bin/ranlib")
    shelltools.export("NATIVE", '.')

def setup():
    exportEnv()

    shelltools.cd("%s/src" % GetWorkdir)
    libtools.libtoolize("--copy --force")

    shelltools.makedirs("%s/build" % GetWorkdir)
    shelltools.cd("%s/build" % GetWorkdir)

    shelltools.system(" %s/src/configure \
                        --without-cxx-runtime-hack \
                        --without-aleph     \
                        --without-bibtex8   \
                        --without-cjkutils  \
                        --without-detex     \
                        --without-dialog    \
                        --without-dtl       \
                        --without-dvi2tty   \
                        --without-dvidvi    \
                        --without-dviljk    \
                        --without-dvipdfm   \
                        --without-dvipdfmx  \
                        --without-dvipng    \
                        --without-dvipos    \
                        --without-dvipsk    \
                        --without-etex      \
                        --without-gsftopk   \
                        --without-lacheck   \
                        --without-lcdf-typetools  \
                        --without-makeindexk      \
                        --without-mkocp-default   \
                        --without-mkofm-default   \
                        --without-musixflx  \
                        --without-omega     \
                        --without-pdfopen   \
                        --without-ps2eps    \
                        --without-ps2pkm    \
                        --without-psutils   \
                        --without-sam2p     \
                        --without-seetexk   \
                        --without-t1utils   \
                        --without-tetex     \
                        --without-tex4htk   \
                        --without-texi2html \
                        --without-texinfo   \
                        --without-texlive   \
                        --without-ttf2pk    \
                        --without-tth       \
                        --without-xdv2pdf   \
                        --without-xdvik     \
                        --without-xdvipdfmx \
                        --without-xetex     \
                        --disable-largefile \
                        --with-system-zlib \
                        --with-system-pnglib \
                        --with-system-ncurses --with-system-pnglib --with-system-zlib \
                        --with-system-gd --with-system-tifflib --with-system-wwwlib --with-system-t1lib \
                        --with-system-freetype --with-system-freetype2 \
                        --with-freetype2-include=/usr/include/freetype2 \
                        --prefix=/usr" % GetWorkdir)
def build():
    shelltools.cd("%s/build/texk/web2c/" % GetWorkdir)
    exportEnv()

    autotools.make("-j1 \
                    LIBMPLIBDEP='/usr/lib/libmplib/mplib.la' \
                    LDZZIPLIB='%s -lzzip -lz' ZZIPLIBINC=''  \
                    LIBXPDFDEP='' LDLIBXPDF='-lpoppler' \
                    LIBXPDFINCLUDE='-I/usr/include/poppler' LIBXPDFCPPFLAGS='-I/usr/include/poppler' \
                    LIBPNGINCLUDES='-I/usr/include/libpng12' \
                    ZLIBSRCDIR='.' \
                    luatex" % get.LDFLAGS())

def install():
    shelltools.cd("%s/build/texk/web2c/" % GetWorkdir)
    exportEnv()

    autotools.make("bindir='%s/usr/bin' \
                    LIBMPLIBDEP='/usr/lib/libmplib/mplib.la' \
                    LDZZIPLIB='%s -lzzip -lz' ZZIPLIBINC='' \
                    LIBXPDFDEP='' LDLIBXPDF='-lpoppler' \
                    LIBXPDFINCLUDE='-I/usr/include/poppler' LIBXPDFCPPFLAGS='-I/usr/include/poppler' \
                    LIBPNGINCLUDES='-I/usr/include/libpng12' \
                    ZLIBSRCDIR='.' \
                    install-luatex" % (get.installDIR(), get.LDFLAGS()))

    pisitools.dodoc("%s/README" % GetWorkdir, "%s/manual/*.pdf" % GetWorkdir)
