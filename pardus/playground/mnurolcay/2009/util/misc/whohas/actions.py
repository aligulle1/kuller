#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("program/whohas")

    pisitools.doman("usr/share/man/man1/whohas.1")
    pisitools.doman("usr/share/man/de/man1/whohas.1")

    pisitools.dodoc("Changelog", "intro.txt", "LICENSE")
