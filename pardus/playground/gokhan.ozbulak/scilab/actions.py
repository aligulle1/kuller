#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

LibDir = "/usr/lib"
JavaDir = "/opt/sun-jdk"

def get_config_options():
    config_with = [
                    'tk-library=%s' % LibDir, 'tcl-library=%s' % LibDir, 'blas-library=%s' % LibDir,
                    'lapack-library=%s' % LibDir, 'jdk=%s' % JavaDir, 'gfortran',
                    'gcc', 'ocaml', 'fftw', 'hdf5'
                    ]
    config_without = ['pvm']
    config_enable = ['shared', 'build-localization', 'build-help', 'build-swig']
    config_disable = ['rpath', 'static']

    conf = []
    for i in config_with:
        conf.append("--with-%s" % i)
    for i in config_without:
        conf.append("--without-%s" % i)
    for i in config_enable:
        conf.append("--enable-%s" % i)
    for i in config_disable:
        conf.append("--disable-%s" % i)

    return " ".join(conf)

def setup():
    pass

def build():
    autotools.configure("%s" % get_config_options())

def install():
    autotools.make()
