#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="sudo-gettext-1.6.8p12"

def setup():
    autotools.configure("--with-all-insults --disable-path-info --with-env-editor --with-pam")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/etc/pam.d")
    shelltools.copy("sample.pam","%s/etc/pam.d/sudo" % get.installDIR())

    pisitools.dodoc("BUGS", "CHANGES", "HISTORY", "PORTING", "README", "RUNSON", "TODO", "TROUBLESHOOTING", "UPGRADE")

    import glob
    for i in glob.glob("po/*.po"):
        lang = i[3:].split(".")[0]
        pisitools.domo("po/%s.po" % lang, lang, "sudo.mo")
