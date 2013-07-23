#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-debugging \
                         --without-kpathsea \
                         --with-ncsb-dir=/usr/share/fonts/default/ghostscript")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/lilypond/2.10.33/vim/compiler/lilypond.vim", "/usr/share/vim/vim71/compiler/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/ftdetect/lilypond.vim", "/usr/share/vim/vim71/ftdetect/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/ftplugin/lilypond.vim", "/usr/share/vim/vim71/ftplugin/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/indent/lilypond.vim", "/usr/share/vim/vim71/indent/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/syntax/lilypond-words", "/usr/share/vim/vim71/syntax/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/syntax/lilypond-words.vim", "/usr/share/vim/vim71/syntax/")
    pisitools.domove("/usr/share/lilypond/2.10.33/vim/syntax/lilypond.vim", "/usr/share/vim/vim71/syntax/")

    pisitools.removeDir("/usr/share/emacs/site-lisp")
    pisitools.removeDir("/usr/share/lilypond/2.10.33/vim")

    pythonmodules.fixCompiledPy("/usr/share/lilypond/%s/python" % get.srcVERSION())
    pisitools.dodoc("COPYING", "ChangeLog", "NEWS.txt", "README.txt")
