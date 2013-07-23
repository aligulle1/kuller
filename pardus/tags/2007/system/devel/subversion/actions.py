#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
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

    # Respect the user LDFLAGS
    shelltools.export("EXTRA_LDFLAGS", get.LDFLAGS())

def build():
    autotools.make("external-all")
    autotools.make("LT_LDFLAGS=\"-L%s/usr/lib\" local-all" % get.installDIR())
    autotools.make("swig-py")

    pisitools.dosed("svn-config", "@SVN_DB_[^@]*@")

def install():
    shelltools.export("PYTHON_DIR", "/usr/lib/%s" % get.curPYTHON())
    
    # install svn
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("svn-config")

    # install swig-py
    autotools.rawInstall("DESTDIR=%s DISTUTIL_PARAM=--prefix=%s LD_LIBRARY_PATH=\"-L%s/usr/lib\"" % \
                        (get.installDIR(), get.installDIR(), get.installDIR()), "install-swig-py")

    # Move py/c'into proper dir
    pisitools.domove("/usr/lib/svn-python/svn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/svn-python/libsvn", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.removeDir("/usr/lib/svn-python")

    # some helper tools
    pisitools.insinto("/usr/bin/", "tools/backup/hot-backup.py", "svn-hot-backup")
    pisitools.insinto("/usr/bin/", "contrib/client-side/svn_load_dirs.pl", "svn-load-dirs")
    pisitools.insinto("/usr/bin/", "contrib/client-side/svnmerge.py", "svnmerge")
    shelltools.chmod("%s/usr/bin/svnmerge" % get.installDIR(), 0755)
 
    # Documentation and etc.
    pisitools.dodoc("BUGS", "COMMITTERS", "COPYING", "HACKING", "INSTALL", "README", \
        "CHANGES", "tools/xslt/svnindex.css", "tools/xslt/svnindex.xsl")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcTAG()), "contrib")
