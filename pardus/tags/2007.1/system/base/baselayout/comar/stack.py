#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2006, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. Please read the COPYING file.
#

import os
import re
import string
import subprocess

rc_path = "/etc/resolv.conf"
name_path = "/etc/env.d/01hostname"
hosts_path = "/etc/hosts"
env_cmd = "/sbin/update-environment"
host_cmd = "/usr/bin/hostname %s"
valid_name_chars = string.ascii_letters + string.digits + '.' + '_' + '-'

def getDefs():
    dict = get_profile("Net.Stack.setNameServers")
    if dict and dict.has_key("nameservers"):
        defs = dict["nameservers"].split("\n")
    else:
        defs = []
        for line in file(rc_path):
            if line.startswith("nameserver "):
                defs.append(line.split(" ", 1)[1].rstrip("\n"))
        # Record these in the profile as defaults
        import comar
        com = comar.Link()
        com.Net.Stack.setNameServers(nameservers="\n".join(defs))
    return defs

def getNameServers():
    return "\n".join(getDefs())

def setNameServers(nameservers=None):
    f = file(rc_path)
    list = filter(lambda x: not "nameserver" in x, f.readlines())
    f.close()
    servers = map(lambda x: "nameserver %s\n" % x, nameservers.split("\n"))
    f = file(rc_path, "w")
    f.write("".join(list) + "".join(servers))
    f.close()

def useNameServers(nameservers=None):
    defs = getDefs()
    if nameservers and nameservers != "":
        temp = nameservers.split("\n")
        temp.extend(defs)
        defs = temp
    setNameServers("\n".join(defs))

def getHostNames():
    dict = get_profile("Net.Stack.setHostNames")
    if dict and dict.has_key("hostnames"):
        return dict["hostnames"]
    # If not set by user in profile, query the system
    cmd = subprocess.Popen(["/usr/bin/hostname"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    a = cmd.communicate()
    if a[1] == "":
        return a[0].rstrip("\n")
    return ""

def setHostNames(hostnames=None):
    if not hostnames:
        return
    invalid = filter(lambda x: not x in valid_name_chars, hostnames)
    if len(invalid) > 0:
        fail("Invalid characters '%s' in hostname" % ("".join(invalid)))
    
    # hostname
    f = file(name_path)
    data = f.read()
    f.close()
    data = re.sub('HOSTNAME="(.*)"', 'HOSTNAME="%s"' % hostnames, data)
    f = file(name_path, "w")
    f.write(data)
    f.close()
    
    # hosts
    f = file(hosts_path)
    data = f.readlines()
    f.close()
    f = file(hosts_path, "w")
    flag = 1
    for line in data:
        if line.startswith("127.0.0.1"):
            line = "127.0.0.1 localhost %s\n" % hostnames
            flag = 0
        f.write(line)
    if flag:
        f.write("127.0.0.1 localhost %s\n" % hostnames)
    f.close()
    
    # update environment
    os.system(env_cmd)
    
    # we dont call the following command, it mess up system
    # hostname changes take effect after restart
    #os.system(host_cmd % hostnames)
