# name: actions.py template
# key: action
# binding: direct-keybinding
# --
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright ${1:2010} TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

${2:#}WorkDir = "$3"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
${4:pass}

def build():
${5:pass}

def check():
${6:pass}

def install():
${7:pass}

