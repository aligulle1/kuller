#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."
version="4.1.2"

def install():
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % version, "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % version, "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s" % version, "docbook.cat")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-%s/ent" % version, "ent/*.ent")

    pisitools.dodoc("ChangeLog", "README")
