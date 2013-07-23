#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "cakephp-cakephp-f6748d4"

def install():
    pisitools.insinto("/usr/share/php5/cakephp/", "*")
    shelltools.copy(".htaccess", "%s/usr/share/php5/cakephp/.htaccess" % get.installDIR())

    pisitools.remove("/usr/share/php5/cakephp/cake/console/cake.bat")

    pisitools.dosym("/usr/share/php5/cakephp/cake/console/cake", "/usr/bin/cake")
    pisitools.dosym("/usr/share/php5/cakephp/app/tmp/logs", "/var/log/cakephp")

    pisitools.dodoc("README", "cake/LICENSE.txt", "cake/VERSION.txt")

    # Delete redundant doc files
    pisitools.remove("/usr/share/php5/cakephp/README")
    pisitools.remove("/usr/share/php5/cakephp/cake/LICENSE.txt")
    pisitools.remove("/usr/share/php5/cakephp/cake/VERSION.txt")
