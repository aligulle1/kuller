#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "vim71"

def setup():
    pisitools.dosed("runtime/tools/mve.awk", "#!/usr/bin/nawk -f", "#!/usr/bin/awk -f")

    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")

    pisitools.dosed("runtime/doc/syntax.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/tagsrch.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/usr_29.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/menu.vim", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("src/configure.in", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")

    pisitools.dosed("src/configure.in", " libc\.h ", " ")
    pisitools.dosed("src/Makefile", " auto.config.mk:", ":")

    pisitools.remove("src/auto/configure")

    autotools.make("-C src autoconf")

    autotools.configure("--with-features=huge \
                         --enable-multibyte \
                         --enable-perlinterp \
                         --enable-pythoninterp \
                         --enable-gui=yes \
                         --with-tlib=ncurses \
                         --disable-acl \
                         --with-x")

def build():
    autotools.make("-C src auto/osdef.h objects")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/etc/vim")
    pisitools.dodir("/usr/share")
    pisitools.dodir("/usr/share/man")
    pisitools.dodir("/usr/share/vim")

    shelltools.cd("src/")
    autotools.rawInstall("installruntime \
                          installmacros \
                          installtutor \
                          installtools \
                          install-languages \
                          install-icons \
                          DESTDIR=%s \
                          BINDIR=/usr/bin \
                          MANDIR=/usr/share/man \
                          DATADIR=/usr/share" % get.installDIR())
    shelltools.cd("../")

    pisitools.dobin("src/vim")
    pisitools.dosym("/usr/bin/vim", "/usr/bin/vi")
    # gdb looks at /bin/ex for editing, it should be linked to /usr/bin/vim
    pisitools.dosym("/usr/bin/vim", "/bin/ex")
