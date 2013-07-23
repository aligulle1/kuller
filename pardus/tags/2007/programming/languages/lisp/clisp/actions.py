#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

config = "--with-dynamic-ffi \
          --with-module=wildcard \
          --with-module=rawsock \
          --with-module=clx/new-clx \
          --with-module=pcre \
          --with-module=zlib"

cflags = "-W -Wswitch -Wcomment -Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-sign-compare -O2 -fexpensive-optimizations -DUNICODE -DDYNAMIC_FFI -I."
          
def setup():
    shelltools.export("CFLAGS","%s" % cflags)
    autotools.rawConfigure("--prefix=/usr %s build" % config)

def build():
    shelltools.cd("build")
    shelltools.system("./makemake %s --srcdir=../src > Makefile" % config)
    
    autotools.make("config.lisp")
    autotools.make()
    
def install():
    shelltools.cd("build")
    autotools.make("DESTDIR=%s prefix=/usr install-bin" % (get.installDIR()))
    shelltools.cd("..")

    pisitools.removeDir("/usr/lib/clisp/base/")
    pisitools.dosym("/usr/lib/clisp/full","/usr/lib/clisp/base")

    pisitools.dohtml("doc/impnotes.css","doc/impnotes.html","build/clisp.html","doc/clisp.png")
    pisitools.dodoc("build/clisp.ps","build/clisp.pdf","doc/editors.txt","doc/CLOS-guide.txt","doc/LISP-tutorial.txt")

