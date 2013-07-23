#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import tarfile
import os
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"


def install():
    # original script in eagle-lin-x.y.z.run is inefficient
    # so just open the file and find line
    # __DATA__
    #just after that line there starts tar.bz2 file
    runfile = file('eagle-lin-%s.run' % get.srcVERSION(), 'rb')
    line  = ''
    while line != '__DATA__\n':
        line = runfile.readline()
    tf = tarfile.open(fileobj=runfile, mode='r|bz2', bufsize=65536)
    tf.extractall(path="%s/opt/" % get.installDIR())
    tf.close()
    runfile.close()
    #now the eagle is unpacked
    eagledir = "%s/opt/eagle" % get.installDIR()
    #rename /opt/eagle-x.y.z to /opt/eagle
    os.rename("%s-%s" % (eagledir, get.srcVERSION()), eagledir)
    #users have to have writable bin directory,
    #because license file is written here on first run
    shelltools.chown(eagledir, gid="users")
    shelltools.chmod("%s/bin" % eagledir, 0775)
    #make symlinks
    pisitools.dosym("/opt/eagle/bin/eagle", "/usr/bin/eagle")
    pisitools.dosym("/opt/eagle/bin/eagleicon50.png", "/usr/share/pixmaps/eagle.png")
