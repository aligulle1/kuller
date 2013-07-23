#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    pisitools.dosed("GDALmake.opt.in", "@datadir@", "@datadir@/gdal")

    autotools.configure("--with-libz \
                         --with-grass=no \
                         --without-libtool \
                         --with-local=/usr \
                         --with-pic \
                         --with-libgrass=no \
                         --with-cfitsio=yes \
                         --with-pcraster=internal \
                         --with-netcdf \
                         --with-png \
                         --with-libtiff \
                         --with-geotiff=/usr/lib \
                         --with-jpeg \
                         --with-gif \
                         --with-ogdi=/usr/lib/ogdi \
                         --without-hdf5 \
                         --with-jasper \
                         --with-mrsid=no \
                         --with-jp2mrsid=yes \
                         --without-bsb \
                         --without-mysql \
                         --with-xerces \
                         --with-odbc \
                         --with-sqlite \
                         --without-pg \
                         --with-ogr \
                         --with-static-proj4 \
                         --with-geos \
                         --without-php \
                         --with-perl \
                         --with-ruby \
                         --with-python")

def build():
    autotools.make("-j1")

    shelltools.cd("swig/ruby")
    autotools.make()

def install():
    pisitools.dodir("/usr/lib/ruby/site_ruby/1.8/i686-linux/gdal")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COMMITERS", "HOWTO-RELEASE", "NEWS", "PROVENANCE.TXT", "VERSION")
