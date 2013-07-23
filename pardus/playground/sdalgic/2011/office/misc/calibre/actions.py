#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcNAME()
installdir = get.installDIR()
sharedir = "/%s" % get.dataDIR()

shelltools.export("HOME", get.workDIR())
shelltools.export("CC", get.CC())
shelltools.export("CXX", get.CXX())
shelltools.export("OVERRIDE_CFLAGS", "%s %s" % (get.CFLAGS(), get.LDFLAGS()))

shelltools.export("XDG_DATA_DIRS", "%s/%s" % (installdir, sharedir))
# In order to avoid sandbox violations.
shelltools.export("XDG_UTILS_INSTALL_MODE", "system")
#shelltools.export("XDG_UTILS_INSTALL_MODE", "user")

def setup():
    # We have these fonts in liberation-fonts package
    shelltools.unlinkDir("resources/fonts/liberation/")

    # remove hardcoded prs500 fonts, so that calibre falls back to
    # using the liberation ones in /usr/share/fonts/
    shelltools.unlinkDir("resources/fonts/prs500")

    # remove shebangs
    for path in ["src/calibre/*/*/*/*.py", "src/calibre/*/*/*.py", "setup/install.py", \
            "src/calibre/*/*.py", "src/calibre/*.py", "src/templite/*.py", \
            "resources/default_tweaks.py", "resources/catalog/section_list_templates.py"]:
        pisitools.dosed(path, "^#!/usr/bin/env.*$", "#!/usr/bin/python")

def build():
    pythonmodules.compile()

def install():
    # create directories for xdg-utils
    for path in ["icons/hicolor", "packages", "mime/packages", "applications",
            "desktop-directories"]:
        pisitools.dodir("%s/%s" % (sharedir, path))

    # create directory for calibre environment module
    # the install script assumes it's there.
    pisitools.dodir("/usr/lib/%s/site-packages" % get.curPYTHON())

    pythonmodules.run('setup.py install --root=%s/usr \
                                        --no-compile \
                                        --prefix=/usr \
                                        --libdir=/usr/lib \
                                        --staging-libdir=%s/usr/lib' % (installdir, installdir))

    # clean out files under /usr/share/mime
    shelltools.system("find %s/%s/mime -maxdepth 1 -type f | xargs rm -f" % (installdir, sharedir))

    # add icons under /usr/share/pixmaps
    pisitools.dosym("%s/calibre/images/library.png" % sharedir, "%s/pixmaps/%s-gui.png" % (sharedir, get.srcNAME()))
    pisitools.dosym("%s/calibre/images/viewer.png" % sharedir, "%s/pixmaps/%s-viewer.png" % (sharedir, get.srcNAME()))

    pisitools.rename("%s/mime/packages/calibre-mimetypes" % sharedir, "calibre-mimetypes.xml")

    # packages aren't allowed to register mimetypes like this
    pisitools.remove("%s/applications/defaults.list" % sharedir)
    #pisitools.remove("%s/applications/mimeinfo.cache" % sharedir)

    # correct man page path
    pisitools.domove("%s/calibre/man/man1/*" % sharedir, "%s/man1/" % get.manDIR())
    pisitools.removeDir("%s/calibre/man" % sharedir)

    # these package are provided externally
    for pkg in ["cherrypy", "pyPdf", "routes"]:
        pisitools.removeDir("/usr/lib/%s/%s" % (get.srcNAME(), pkg))

    # mimetype icon for lrf
    for path in ["mimetypes", "apps"]:
        pisitools.dodir("%s/icons/hicolor/scalable/%s" % (sharedir,path))

    pisitools.insinto("%s/icons/hicolor/scalable/mimetypes" % sharedir, \
                      "resources/images/mimetypes/lrf.png", \
                      "application-x-sony-bbeb.png")

    pisitools.insinto("%s/icons/hicolor/scalable/apps" % sharedir, \
                      "resources/images/viewer.png", "viewer.png")

    # move etc/bash_completion.d from /usr/etc to /etc
    pisitools.domove("/usr/etc", "/")

    pisitools.remove("/usr/bin/calibre-uninstall")

    pisitools.removeDir("/usr/share/desktop-directories")
    pisitools.removeDir("/usr/share/packages")
    pisitools.removeDir("/usr/share/calibre/fonts")

