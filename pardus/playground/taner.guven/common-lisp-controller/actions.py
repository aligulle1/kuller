# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    pass

def install():
    pisitools.doexe("clc-lisp", "usr/bin")
    pisitools.doexe("clc-register-user-package", "usr/bin")
    pisitools.doexe("clc-slime", "usr/bin")
    pisitools.doexe("clc-unregister-user-package", "usr/bin")

    pisitools.doexe("clc-clbuild", "usr/sbin")
    pisitools.doexe("clc-update-customized-images", "usr/sbin")
    pisitools.doexe("register-common-lisp-implementation", "usr/sbin")
    pisitools.doexe("register-common-lisp-source", "usr/sbin")
    pisitools.doexe("unregister-common-lisp-implementation", "usr/sbin")
    pisitools.doexe("unregister-common-lisp-source", "usr/sbin")


    pisitools.dolib("common-lisp-controller.lisp", "usr/share/common-lisp/source/common-lisp-controller")
    pisitools.dolib("post-sysdef-install.lisp", "usr/share/common-lisp/source/common-lisp-controller")


