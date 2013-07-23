#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("conf-home","/usr/local","/usr")

def build():
    shelltools.system("make")

def install():
    pisitools.insinto("/etc", "dnsroots.global")
    bin_list = ['axfrdns-conf','dnscache-conf','pickdns-conf','rbldns-conf',
                'tinydns-conf','walldns-conf','dnscache','tinydns','walldns',
                'rbldns','pickdns', 'axfrdns','axfr-get','tinydns-get',
                'pickdns-data','rbldns-data','tinydns-data','tinydns-edit',
                'dnsip','dnsipq','dnsname','dnstxt','dnsmx','dnsfilter',
                'random-ip','dnsqr','dnsq','dnstrace', 'dnstracesort']
    for bin in bin_list:
        pisitools.dobin(bin, "/usr/bin")
    pisitools.dodoc("CHANGES","FILES","README","SYSDEPS","TARGETS","TODO","VERSION")
