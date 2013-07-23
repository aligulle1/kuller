#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    # Respect the user LDFLAGS
    shelltools.export("EXTRA_LDFLAGS", get.LDFLAGS())

    autotools.configure("--disable-static \
                         --with-apxs2 \
                         --with-swig \
                         --with-zlib \
                         --with-ssl \
                         --with-berkeley-db \
                         --with-python \
                         --with-neon=/usr \
                         --with-apr=/usr \
                         --with-apr-util=/usr \
                         --enable-nls \
                         --disable-experimental-libtool \
                         --disable-mod-activation")

def build():
    autotools.make("external-all")
    autotools.make("LT_LDFLAGS=\"-L%s/usr/lib\" local-all" % get.installDIR())

    # python bindings
    autotools.make("swig-py")

    # perl bindings (needed by git-svn*)
    autotools.make("swig-pl")

    pisitools.dosed("svn-config", "@SVN_DB_[^@]*@")

def install():
    # install svn
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("svn-config")

    # install swig-py
    shelltools.export("PYTHON_DIR", "/usr/lib/%s" % get.curPYTHON())
    autotools.rawInstall("DESTDIR=%s DISTUTIL_PARAM=--prefix=%s LD_LIBRARY_PATH=\"-L%s/usr/lib\"" % \
                        (get.installDIR(), get.installDIR(), get.installDIR()), "install-swig-py")

    # install swig-pl
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-swig-pl")

    # Move py/c'into proper dir
    pisitools.domove("/usr/lib/svn-python/svn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/svn-python/libsvn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/svn-python")

    # some helper tools
    pisitools.insinto("/usr/bin", "tools/backup/hot-backup.py", "svn-hot-backup")
    pisitools.insinto("/usr/bin", "contrib/client-side/svn_load_dirs.pl", "svn-load-dirs")
    pisitools.insinto("/usr/bin", "contrib/client-side/svnmerge.py", "svnmerge")
    shelltools.chmod("%s/usr/bin/svnmerge" % get.installDIR(), 0755)

    perlmodules.fixLocalPod()

    # Documentation and etc.
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "contrib")
    pisitools.dodoc("BUGS", "COMMITTERS", "COPYING", "HACKING", "README", "CHANGES")
