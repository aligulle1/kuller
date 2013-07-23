#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-debugging \
                         --with-ncsb-dir=/usr/share/fonts/default/ghostscript")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()

    pisitools.domove("/usr/share/lilypond/2.8.7/vim/compiler/lilypond.vim", "/usr/share/vim/vim70/compiler/lilypond.vim")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/ftdetect/lilypond.vim", "/usr/share/vim/vim70/ftdetect/lilypond.vim")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/ftplugin/lilypond.vim", "/usr/share/vim/vim70/ftplugin/lilypond.vim")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/indent/lilypond.vim", "/usr/share/vim/vim70/indent/lilypond.vim")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/syntax/lilypond-words", "/usr/share/vim/vim70/syntax/lilypond-words")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/syntax/lilypond-words.vim", "/usr/share/vim/vim70/syntax/lilypond-words.vim")
    pisitools.domove("/usr/share/lilypond/2.8.7/vim/syntax/lilypond.vim", "/usr/share/vim/vim70/syntax/lilypond.vim")
    pisitools.remove("/usr/share/emacs/site-lisp")
    pisitools.dodoc("COPYING", "ChangeLog", "NEWS.txt", "README.txt")
