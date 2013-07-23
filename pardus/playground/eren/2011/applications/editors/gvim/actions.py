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
                         --enable-gui=gtk2 \
                         --with-x \
                         --with-tlib=ncurses \
                         --disable-xim \
                         --disable-acl")

def build():
    autotools.make("-C src auto/osdef.h objects")

def install():
    pisitools.dodir("/usr/bin")

    shelltools.cd("src/")
    autotools.rawInstall("installruntime \
                          DESTDIR=%s \
                          BINDIR=/usr/bin \
                          MANDIR=/usr/share/man \
                          DATADIR=/usr/share" % get.installDIR())
    shelltools.cd("../")

    # we only need vim binary that is linked against GTK2
    # gvim depends on vim, /usr/share/vim is common directory, so it should be deleted
    pisitools.removeDir("/usr/share/vim")

    # remove manpages too, it's extracted from vim
    pisitools.removeDir("/usr/share/man")

    # remove binaries that are also in vim
    for bin in ["eview", "evim", "ex", "view", "rview", "rvim", "vimdiff", "vimtutor", "xxd"]:
        pisitools.remove("/usr/bin/%s" % bin)

    # remove pre-linked binaries, we should link it manually to vim-gtk
    pre_linked = ["gview", "gvim", "gvimdiff", "rgview", "rgvim"]
    for bin in pre_linked:
        pisitools.remove("/usr/bin/%s" % bin)

    # rename vim binary to vim-gtk
    pisitools.rename("/usr/bin/vim", "vim-gtk")

    # do linking
    for bin in pre_linked:
        pisitools.dosym("/usr/bin/vim-gtk", "/usr/bin/%s" % bin)
