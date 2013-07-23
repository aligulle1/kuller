#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LC_ALL", "C")

    shelltools.system("sh Configure -des \
                      -Darchname=i686-linux \
                      -Dcccdlflags=-fPIC \
                      -Dccdlflags=-rdynamic \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize=\"%s\" \
                      -Duselargefiles \
                      -Dd_dosuid \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.1.5.8 \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dinc_version_list=5.8.0 5.8.0/i686-linux 5.8.2 5.8.2/i686-linux 5.8.4 5.8.4/i686-linux \
                      -Dcf_by=Pardus \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db" %(get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR()))

def build():
    autotools.make("-j1")

def install():
    shelltools.export("LC_ALL", "C")

    pisitools.dodir("/usr/lib/perl5/5.8.8/i686-linux/CORE")
    pisitools.dosym("../../../../libperl.so.1.5.8", "/usr/lib/perl5/5.8.8/i686-linux/CORE/libperl.so.1.5.8")
    pisitools.dosym("../../../../libperl.so.1.5.8", "/usr/lib/perl5/5.8.8/i686-linux/CORE/libperl.so.1")
    pisitools.dosym("../../../../libperl.so.1.5.8", "/usr/lib/perl5/5.8.8/i686-linux/CORE/libperl.so")

    pisitools.dodir("/usr/lib/perl5/site_perl/5.8.8/i686-linux")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/perl")
    pisitools.dosym("perl5.8.8", "/usr/bin/perl")

    # This is to fix a missing c flag for backwards compat
    pisitools.dosed("%s/usr/lib/perl5/5.8.8/i686-linux/Config.pm" % get.installDIR(), "ccflags='", "ccflags='-DPERL5 ")
    pisitools.dosed("%s/usr/lib/perl5/5.8.8/i686-linux/Config.pm" % get.installDIR(), "cppflags='", "cppflags='-DPERL5 ")

    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "Todo*", "AUTHORS")

    pisitools.dodir("/usr/share/doc/%s/html" % get.srcTAG())

    shelltools.system("./perl installhtml \
                        --podroot='.' \
                        --podpath='lib:ext:pod:vms' \
                        --recurse \
                        --htmldir=\"%s/usr/share/doc/%s/html\" \
                        --libpods='perlfunc:perlguts:perlvar:perlrun:perlop'" % (get.installDIR(), get.srcTAG()))

    # Perl5 library
    pisitools.dolib("libperl.so.1.5.8")
    libtools.preplib()

    # Remove duplicated docs
    pisitools.remove("/usr/share/man/man3/Digest::MD5.3pm")
    pisitools.remove("/usr/share/man/man3/Digest.3pm")
    pisitools.remove("/usr/share/man/man3/Digest::base.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Netrc.3pm")
    pisitools.remove("/usr/share/man/man3/Net::libnetFAQ.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Config.3pm")
    pisitools.remove("/usr/share/man/man3/Net::FTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::NNTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Time.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Domain.3pm")
    pisitools.remove("/usr/share/man/man3/Net::POP3.3pm")
    pisitools.remove("/usr/share/man/man3/Net::SMTP.3pm")
    pisitools.remove("/usr/share/man/man3/Net::Cmd.3pm")
    pisitools.remove("/usr/share/man/man3/MIME::Base64.3pm")
    pisitools.remove("/usr/share/man/man3/MIME::QuotedPrint.3pm")
    pisitools.remove("/usr/share/man/man3/Time::HiRes.3pm")
