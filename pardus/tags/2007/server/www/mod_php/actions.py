#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "php-5.2.0"

def setup():
    # Thanks to Arman Aksoy for this tip
    shelltools.export("LC_ALL", "C")

    pisitools.dosed("configure.in", "PHP_UNAME=`uname -a | xargs`", "PHP_UNAME='Pardus Linux 1.1'")
    pisitools.dosed("ext/pgsql/config.m4", "include/postgresql", " include/postgresql/pgsql")

    # Don't touch apache.conf
    for i in ["configure", "sapi/apache/config.m4", "sapi/apache2filter/config.m4", "sapi/apache2handler/config.m4"]:
        pisitools.dosed(i, "-i -a -n php5", "-i -n php5")
        pisitools.dosed(i, "-i -A -n php5", "-i -n php5")

    autotools.configure("--sysconfdir=/etc \
                         --cache-file=./config.cache \
                         --with-config-file-path=/etc/php \
                         --with-config-file-scan-dir=/etc/php/ext \
                         --with-pear=/usr/share/php5/PEAR \
                         --with-apxs2=/usr/sbin/apxs2 \
                         --with-zlib-dir=/usr/lib \
                         --with-libxml-dir=/usr/lib \
                         --with-libxml2=/usr/lib \
                         --without-xpm \
                         --with-jpeg-dir=/usr/lib/ \
                         --with-png-dir=/usr/lib/ \
                         --with-freetype-dir=/usr \
                         --enable-cli \
                         --disable-cgi \
                         --enable-memory-limit \
                         --enable-so \
                         --with-zend-vm=GOTO \
                         --with-zend-vm=SWITCH \
                         %s" % extensions())

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=\"%s\"" % get.installDIR(), "install")
    autotools.rawInstall("INSTALL_ROOT=\"%s\"" % get.installDIR(), "install-sapi")

    pisitools.insinto("/etc/php/", "php.ini-dist", "php.ini")

    pisitools.dosed("%s/etc/php/php.ini" % get.installDIR(), "(extension_dir = .*)", ";\\1")
    pisitools.dosed("%s/etc/php/php.ini" % get.installDIR(), r";include_path = \".:/php/includes\"",
                                                             "include_path = \".:/usr/share/php5/PEAR\"")

def extensions():
    disabled = [
        'ctype'
    ]
    enabled = [
        'exif', 'ftp', 'soap', 'sockets', 'sqlite-utf8', 'bcmath',
        'dom', 'wddx', 'tokenizer', 'simplexml', 'mbstring', 'calendar',
        'gd-native-ttf'
    ]
    shared = [
        'zlib', 'dba', 'dbase', 'embedded-mysqli'
    ]
    with = [
        'bz2', 'curl', 'iconv', 'mysql', 'mysqli', 'kerberos', 'sqlite', 'mime-magic',
        'xml-reader', 'xsl', 'curlwrappers', 'gdbm', 'db4', 'inifile', 'ldap',
        'flatfile', 'gd', 'ttf', 'gettext', 'ncurses', 'regex=php', 'pic', 'pcre-regex'
    ]
    without = []

    conf = []
    for i in disabled:
        conf.append("--disable-%s" % i)
    for i in enabled:
        conf.append("--enable-%s " % i)
    for i in shared:
        conf.append("--enable-%s=shared" % i)
    for i in with:
        conf.append("--with-%s" % i)
    for i in without:
        conf.append("--without-%s" % i)

    return ' '.join(conf)
