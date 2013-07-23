# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

stumpwm_src_dir = "%s/common-lisp/source/stumpwm" % get.dataDIR()

def setup():
    autotools.autoconf()
    autotools.configure("--with-clisp=/usr/bin/clisp \
                        --with-ppcre=/usr/share/common-lisp/source/cl-ppcre \
                        --with-contrib-dir=%s/contrib" % stumpwm_src_dir)

def build():
    shelltools.system("XDG_CACHE_HOME=$(pwd)/.cache make stumpwm.info")

def install():
    pisitools.insinto(stumpwm_src_dir, "stumpwm.asd")
    pisitools.insinto(stumpwm_src_dir, "*.lisp")

    pisitools.remove("%s/asdf.lisp" % stumpwm_src_dir)
    pisitools.remove("%s/make-image.lisp" % stumpwm_src_dir)

    pisitools.domove("/usr/share/common-lisp/source/stumpwm/sample-stumpwmrc.lisp",
                     "%s/stumpwm/examples" % get.docDIR())

    pisitools.insinto("%s/contrib" % stumpwm_src_dir, "contrib/*.lisp")

    pisitools.insinto("/usr/bin", "contrib/stumpish")
    pisitools.insinto("%s/stumpwm" % get.docDIR(), "contrib/stumpwm-mode.el")

    pisitools.doinfo("stumpwm.info")

    pisitools.dodoc("AUTHORS", "COPYING", "HACKING", "NEWS", "README")

