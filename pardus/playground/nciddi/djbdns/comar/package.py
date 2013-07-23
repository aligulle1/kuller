#!/usr/bin/python

import os
import pwd

djbdns_users = ['dnslog', 'dnscache', 'tinydns']

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for user in djbdns_users:
        try:
            pwd.getpwnam(user)
        except KeyError:
            for uid in range(101,999):
                try:
                    pwd.getpwuid(uid)
                except KeyError:
                    os.system("/usr/sbin/useradd -d /dev/null -g nofiles -u %s -s /bin/false %s" % (uid,user))
                    break

def preRemove():
    for user in djbdns_users:
        try:
            pwd.getpwnam(user)
        except KeyError:
            break
        os.system("/usr/sbin/userdel %s" % user)
    os.system("/bin/rm /service/dnscache")
