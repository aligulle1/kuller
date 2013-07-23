#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools

WorkDir = "xmms2-0.4DrKosmos"

def setup():
    shelltools.system("./waf configure --prefix=/usr")

def build():
    shelltools.system("./waf build")

def install():
    pass
    """
    shelltools.system("./waf install")

    # copy default configuration file, and set it to non-readable by others since it may contain password
    pisitools.insinto("/etc", "doc/mpdconf.example", "mpd.conf")

    # remove built-in files and add these to valid directory
    pisitools.removeDir("/usr/share/doc/mpd")
    pisitools.dodoc("AUTHORS", "README", "COMMANDS", "TODO")
    """
