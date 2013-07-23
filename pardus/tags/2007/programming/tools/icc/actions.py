#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="l_cc_c_%s/data" % get.srcVERSION()
version_simple = (get.srcVERSION()).replace('.','')

def setup():
    shelltools.system("rpm2targz intel-icc%s-%s-1.i386.rpm" % (version_simple,get.srcVERSION()))
    shelltools.system("tar xvf intel-icc%s-%s-1.i386.tar.gz" % (version_simple,get.srcVERSION()))

def install():
    pisitools.insinto("/","opt")

    pisitools.dosed("%s/opt/intel/cc/*/bin/*" % get.installDIR(),"<INSTALLDIR>","/opt/intel/cc/%s" % get.srcVERSION())

    # Work around Turkish problems with FlexLM, Intel Premier Support Issue #366034
    for app in ["icc","icpc"]:
        pisitools.dosed("%s/opt/intel/cc/*/bin/%s" % (get.installDIR(),app),"#!/bin/sh","#!/bin/sh\n\nexport LC_ALL=C");

    # Empty licenses directory
    pisitools.dodir("/opt/intel/licenses")
