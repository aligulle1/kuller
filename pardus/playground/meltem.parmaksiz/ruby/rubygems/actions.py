#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os 

#ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]'
ruby_sitelib = "/usr/lib/ruby/site_ruby/1.8/"


def get_file_permission(name):
    f = open(name, "r").readline()
    return  0755 if f.startswith("#!") else 0644


def install():
    pisitools.dobin("bin/gem")
    pisitools.insinto("%s" % ruby_sitelib, "lib/*")

    directory = "%s%s" % (get.installDIR(), ruby_sitelib)
    for root, dirs, files in os.walk(directory):
        for name in files:
            pisitools.dosed(os.path.join(root, name), "#!/usr/bin/env ruby" , "#!/usr/bin/ruby")
            shelltools.chmod(os.path.join(root, name), get_file_permission(os.path.join(root, name)))
