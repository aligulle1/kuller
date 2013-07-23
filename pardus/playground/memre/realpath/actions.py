#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make('VERSION="1.16" SUBDIRS="src man"')

def install():
    autotools.install('VERSION="1.16" SUBDIRS="src man" DESTDIR=%s' % get.installDIR())

