# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.

# standard python modules
import os

import gettext
__trans = gettext.translation('pisi', fallback=True)
_ = __trans.ugettext

# Pisi Modules
import pisi.context as ctx

# ActionsAPI Modules
import pisi.actionsapi
import pisi.actionsapi.get as get
from pisi.actionsapi.shelltools import system, cd
from pisi.actionsapi.pisitools import dodir


class InstallError(pisi.actionsapi.Error):
    def __init__(self, value=''):
        pisi.actionsapi.Error.__init__(self, value)
        self.value = value
        ctx.ui.error(value)

def install(package = get.srcNAME(), prefix = get.installDIR(), r_home = '/usr/lib/R'):
    dodir("%s/library" % r_home)
    cd(get.workDIR())
    if system('/usr/bin/R CMD INSTALL %s -l %s/%s/library' % (package, prefix, r_home)):
        raise InstallError(_('Install failed.'))
