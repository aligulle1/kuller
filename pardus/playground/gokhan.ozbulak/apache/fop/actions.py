#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir="fop-1.0"

def install():
    pisitools.dodir("/opt/fop-1.0")
    pisitools.insinto("/opt/fop-1.0", "./*")

    for root, dirs, files in os.walk("lib"):
        for name in files:
            if name.endswith(".jar"):
                if not name.startswith("xml-apis"):
                    libPath = "/usr/share/java"
                else:
                    libPath = "/usr/share/java/xml-apis"
                pisitools.dolib("lib/%s" % (name), libPath)
                pisitools.dosym(name, os.path.join(libPath, "%s.jar" % (name[:name.rfind("-")])))

    ''' Doc for main package '''
    pisitools.dodoc("KEYS", "LICENSE", "NOTICE", "README")
    ''' Html for main package '''
    pisitools.dohtml("docs/*")

    ''' Doc for sub-packages '''
    pisitools.dodoc("lib/avalon-framework.LICENSE.txt", "lib/avalon-framework.NOTICE.TXT", destDir="avalon")
    pisitools.dodoc("lib/batik.LICENSE.txt", "lib/batik.NOTICE.txt", destDir="batik")
    pisitools.dodoc("lib/commons-io.LICENSE.txt", "lib/commons-io.NOTICE.txt", destDir="commons-io")
    pisitools.dodoc("lib/commons-logging.LICENSE.txt", "lib/commons-logging.NOTICE.txt", destDir="commons-logging")
    pisitools.dodoc("lib/serializer.LICENSE.txt", "lib/serializer.NOTICE.txt", destDir="serializer")
    pisitools.dodoc("lib/xalan.BCEL.LICENSE.txt", "lib/xalan.LICENSE.txt", "lib/xalan.NOTICE.txt", "lib/xalan.regexp.LICENSE.txt", "lib/xalan.runtime.LICENSE.txt", destDir="xalan")
    pisitools.dodoc("lib/xercesImpl.LICENSE.txt", "lib/xercesImpl.NOTICE.txt", "lib/xerces.LICENSE.txt", destDir="xerces")
    pisitools.dodoc("lib/xml-apis-ext.LICENSE.dom-documentation.txt", "lib/xml-apis-ext.LICENSE.dom-software.txt", "lib/xml-apis-ext.LICENSE.txt", "lib/xml-apis-ext.NOTICE.txt", "lib/xml-apis-ext.README.dom.txt", "lib/xml-apis.LICENSE.txt", "lib/xml-apis.NOTICE.txt" ,destDir="xml-apis")
    pisitools.dodoc("lib/xmlgraphics-commons.LICENSE.txt", "lib/xmlgraphics-commons.NOTICE.txt", destDir="xmlgraphics-commons")

    ''' Html for sub-packages '''
    pisitools.dohtml("lib/xml-apis-ext.LICENSE.sac.html", "lib/xml-apis.LICENSE.DOM-documentation.html", "lib/xml-apis.LICENSE.DOM-software.html", "lib/xml-apis.LICENSE-SAX.html", destDir="xml-apis")

    pisitools.dosym("/opt/fop-1.0/fop", "/usr/bin/fop")

    pisitools.removeDir("opt/fop-1.0/lib")
