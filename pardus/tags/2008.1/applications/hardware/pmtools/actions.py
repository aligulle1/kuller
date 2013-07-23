#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006, 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dosbin("acpidump/acpidump")
    # Rename acpixtract since acpica package has a tool with the same name
    pisitools.insinto("/usr/bin", "acpixtract/acpixtract", "acpixtract-pmtools")
    pisitools.dobin("madt/madt")

    madt_docdir = "%s/%s/madt" % (get.docDIR(), get.srcTAG())
    pisitools.insinto(madt_docdir, "madt/README")
    pisitools.insinto(madt_docdir, "madt/example.*")

    pisitools.dodoc("COPYING", "README")
