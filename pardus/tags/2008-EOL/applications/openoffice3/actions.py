#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "ooo-build-%s" % get.srcVERSION()
NoStrip = ["/opt/OpenOffice.org/lib/ooo-3.1/basis3.1/share", "/opt/OpenOffice.org/lib/ooo-3.1/share"]

UpstreamVersion = "ooo310-m11"

def getJobCount():
    # If jobs field in pisi.conf is greater than 1, use 'this value - 1' as number of cpus. There is also a max-jobs configure opt. but it's buggy now
    return max(int(get.makeJOBS().strip().replace("-j", "")) - 1, 1)

def setup():
    #libdir is needed to set exec_prefix stuff of patches/dev300/system-python-ure-bootstrap.diff
    shelltools.system('./configure \
                       --prefix=/opt/OpenOffice.org \
                       --libdir=/opt/OpenOffice.org/lib \
                       --sysconfdir=/etc \
                       --with-lang="de en-US es fr it nl pt-BR sv tr" \
                       --disable-post-install-scripts \
                       --disable-gtk \
                       --disable-cairo \
                       --disable-mono \
                       --with-distro=PardusCorporate2 \
                       --with-drink=nargile \
                       --with-gcc-speedup=ccache \
                       --with-ant-home=/usr/share/ant \
                       --with-binsuffix=no \
                       --with-system-mdbtools \
                       --with-num-cpus=%s' % getJobCount())

def build():
    shelltools.export("HOME", get.workDIR())
    #TODO: this does not work, find another solution
    #shelltools.export("CLASSPATH", "%s:/usr/share/java/xercesImpl.jar" % os.environ.get("CLASSPATH"))

    #FIXME: parallel build seems not to work well :/
    autotools.make("-j1")

def install():
    shelltools.export("HOME", get.workDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #TODO: Is wrapper still necessary?
    # Remove old links
    #pisitools.remove("/opt/OpenOffice.org/bin/*")
    # New links
    #apps = ["oobase", "oodraw", "oomath", "ooimpress", "oocalc", "oowriter"]
    #for app in apps:
    #    pisitools.dosym("/opt/OpenOffice.org/bin/ooo-wrapper.py", "/usr/bin/%s" % app)

    #dosym main executables
    for bin in map(os.path.basename, shelltools.ls("%s/opt/OpenOffice.org/bin/oo*" % get.installDIR())):
        pisitools.dosym("/opt/OpenOffice.org/bin/%s" % bin, "/usr/bin/%s" % bin)

    #make symlink of unopkg
    pisitools.dosym("/opt/OpenOffice.org/bin/unopkg","/usr/bin/unopkg")

    # Icons
    pisitools.insinto("/usr/share/pixmaps","desktop/48x48/*.png")

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math.png","/usr/share/pixmaps/formula.png")

    #Put pyuno to python directory and add OpenOffice.org python modules directory to sys.path in uno.py
    unoPath = "/opt/OpenOffice.org/lib/ooo-3.1/basis3.1/program/uno.py"
    unopy = open(get.installDIR() + unoPath).read()
    pisitools.dodir("/usr/lib/%s/site-packages/" % get.curPYTHON())
    newunopy = open("%s/usr/lib/%s/site-packages/uno.py" % (get.installDIR(), get.curPYTHON()), "w")
    newunopy.write("import sys\nsys.path.append('/opt/OpenOffice.org/lib/ooo-3.1/basis3.1/program')\n%s" % unopy)
    newunopy.close()
    pisitools.remove(unoPath)
    pisitools.domove("/opt/OpenOffice.org/lib/ooo-3.1/basis3.1/program/unohelper.py", "/usr/lib/%s/site-packages" % get.curPYTHON())

    #install pdfimport, report-builder, wiki-publisher and presenter screen as extensions
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install/", "build/%s/solver/310/unxlngi6.pro/bin/sun-report-builder.oxt" % UpstreamVersion)
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install/", "build/%s/solver/310/unxlngi6.pro/bin/swext/wiki-publisher.oxt" % UpstreamVersion)
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install/", "build/%s/solver/310/unxlngi6.pro/bin/minimizer/sun-presentation-minimizer.oxt" % UpstreamVersion)
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install/", "build/%s/solver/310/unxlngi6.pro/bin/presenter/presenter-screen.oxt" % UpstreamVersion)
    pisitools.insinto("/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install/", "build/%s/solver/310/unxlngi6.pro/bin/pdfimport/pdfimport.oxt" % UpstreamVersion)

    #Fix mktemp directory in unopkg
    pisitools.dosed("%s/opt/OpenOffice.org/lib/ooo-3.1/program/unopkg" % get.installDIR(), "/bin/mktemp", "/usr/bin/mktemp")

    #install man files
    pisitools.domove("/opt/OpenOffice.org/share/man/man1/*", "/usr/share/man/man1")
    pisitools.removeDir("/opt/OpenOffice.org/share/man")

    pisitools.dodoc("AUTHORS","ChangeLog","COPYING","NEWS","README")
