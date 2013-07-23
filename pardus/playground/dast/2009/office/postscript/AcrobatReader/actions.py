#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import tarfile
import os
import shutil
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "AdobeReader"
NoStrip = "/"


def install():
    # original INSTALL script is inefficient
    commonTar = tarfile.open(name="COMMON.TAR", mode='r', bufsize=1024*1024)
    commonTar.extractall(path="%s/opt/" % get.installDIR())
    commonTar.close()
    ilinxrTar = tarfile.open(name="ILINXR.TAR", mode='r', bufsize=1024*1024)
    ilinxrTar.extractall(path="%s/opt/" % get.installDIR())
    ilinxrTar.close()
    # now the Acrobat Reader is unpacked

    # move (rename) /opt/Adobe/Reader9 to /opt/AcrobatReader
    # note: pisitools.domove("/opt/Adobe/Reader9", "/opt/AcrobatReader") does not work for this case
    cwd = os.getcwd()
    os.chdir(get.installDIR())
    os.rename("opt/Adobe/Reader9", "opt/AcrobatReader")
    os.rmdir("opt/Adobe")
    os.chdir(cwd)

    # move files to correct places
    pisitools.domove("/opt/AcrobatReader/Resource/Support/AdobeReader.desktop", "/usr/share/applications")
    pisitools.domove("/opt/AcrobatReader/Resource/Support/vnd*.desktop", "/usr/share/mimelnk/application")
    pisitools.domove("/opt/AcrobatReader/Resource/Support/AdobeReader.xml", "/usr/share/mime/packages")
    
    for size in ("16x16", "20x20", "22x22", "24x24", "32x32", "36x36", "48x48", "64x64", "96x96", "128x128"):
        pisitools.domove("/opt/AcrobatReader/Resource/Icons/%s/AdobeReader9.png" % size, 
            "/usr/share/icons/hicolor/%s/apps" % size)
        pisitools.domove("/opt/AcrobatReader/Resource/Icons/%s/adobe.pdf.png" % size, 
            "/usr/share/icons/hicolor/%s/mimetypes" % size)
        pisitools.domove("/opt/AcrobatReader/Resource/Icons/%s/vnd*.png" % size, 
            "/usr/share/icons/hicolor/%s/mimetypes" % size)

    # clean up unnecessary files
    pisitools.remove("/opt/AcrobatReader/bin/UNINSTALL")
    pisitools.remove("/opt/AcrobatReader/Browser/install_browser_plugin")
    pisitools.removeDir("/opt/AcrobatReader/Browser/HowTo")
    pisitools.removeDir("/opt/AcrobatReader/Resource/Icons")
    pisitools.removeDir("/opt/AcrobatReader/Resource/Support")

    #browser plugin
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    pisitools.dosym("/opt/AcrobatReader/Browser/intellinux/nppdf.so", "/usr/lib/nsbrowser/plugins/nppdf.so")
    #make symlinks
    pisitools.dosym("/opt/AcrobatReader/bin/acroread", "/usr/bin/acroread")
