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

name_msg = {
    "en": "Ethernet network",
    "tr": "Ethernet ağları"
}

dhcp_fail_msg = {
    "en": "Could not get address",
    "tr": "Adres alınamadı"
}

no_device_msg = {
    "en": "Device is not plugged",
    "tr": "Aygıt takılı değil"
}

import os
from comar import network

# Internal functions

def _get(dict, key, default):
    val = default
    if dict and dict.has_key(key):
        val = dict[key]
    return val

def stopSameDev(myname, myuid):
    conns = instances("name")
    for name in conns:
        if myname == name:
            continue
        dev = Dev(name)
        if myuid != dev.uid:
            continue
        
        notify("Net.Link.stateChanged", name + "\ndown")
        if dev.state == "up":
            set_instance(name=name, state="down")


class Dev:
    def __init__(self, name, want=False):
        dict = get_instance("name", name)
        if want:
            if not dict:
                fail("No such connection")
        self.uid = _get(dict, "device", None)
        self.name = name
        self.ifc = None
        if self.uid:
            self.ifc = network.findInterface(self.uid)
        self.state = _get(dict, "state", "down")
        self.mode = _get(dict, "mode", "auto")
        self.address = _get(dict, "address", None)
        self.mask = _get(dict, "mask", None)
        self.gateway = _get(dict, "gateway", None)
        self.namemode = _get(dict, "namemode", "default")
        self.nameserver = _get(dict, "nameserver", None)
    
    def dns(self):
        if self.namemode == "default":
            srvs = []
        elif self.namemode == "auto":
            srvs = self.ifc.autoNameServers()
            if not srvs:
                srvs = []
        else:
            srvs = [ self.nameserver ]
        # This should be replaced with internal call at some point
        import comar
        com = comar.Link()
        com.Net.Stack.useNameServers(nameservers="\n".join(srvs))
        com.read_cmd()
    
    def up(self):
        ifc = self.ifc
        if self.mode == "manual":
            ifc.setAddress(self.address, self.mask)
            ifc.up()
            if self.gateway:
                route = network.Route()
                route.setDefault(self.gateway)
                self.dns()
            notify("Net.Link.stateChanged", self.name + "\nup")
        else:
            notify("Net.Link.stateChanged", self.name + "\nconnecting")
            ret = ifc.startAuto(timeout="20")
            if ret == 0 and ifc.isUp():
                self.dns()
                addr = ifc.getAddress()[0]
                notify("Net.Link.stateChanged", self.name + "\nup " + unicode(addr))
            else:
                notify("Net.Link.stateChanged", self.name + "\ninaccessible " + _(dhcp_fail_msg))
                fail("DHCP failed")
    
    def down(self):
        ifc = self.ifc
        if self.mode != "manual":
            ifc.stopAuto()
        ifc.down()
        notify("Net.Link.stateChanged", self.name + "\ndown")


# Net.Link API

def kernelEvent(data):
    type, dir = data.split("@", 1)
    if not dir.startswith("/class/net/"):
        return
    devname = dir[11:]
    flag = 1
    
    if type == "add":
        ifc = network.IF(devname)
        if ifc.isWireless():
            return
        devuid = ifc.deviceUID()
        notify("Net.Link.deviceChanged", "added net %s %s" % (devuid, network.deviceName(devuid)))
        conns = instances("name")
        for conn in conns:
            dev = Dev(conn)
            if dev.ifc and dev.ifc.name == devname:
                if dev.state == "up":
                    dev.up()
                    return
                flag = 0
        if flag:
            notify("Net.Link.deviceChanged", "new net %s %s" % (devuid, network.deviceName(devuid)))
    
    elif type == "remove":
        conns = instances("name")
        for conn in conns:
            dev = Dev(conn)
            # FIXME: dev.ifc is not enough :(
            if dev.ifc and dev.ifc.name == devname:
                if dev.state == "up":
                    notify("Net.Link.stateChanged", dev.name + "\ninaccessible " + "Device removed")
        notify("Net.Link.deviceChanged", "removed net %s" % devname)

def linkInfo():
    return """type=net
modes=device,net,auto
name=%s""" % _(name_msg)

def deviceList():
    iflist = []
    for ifc in network.interfaces():
        if ifc.isEthernet() and not ifc.isWireless():
            uid = ifc.deviceUID()
            info = network.deviceName(uid)
            iflist.append("%s %s" % (uid, info))
    return "\n".join(iflist)

def scanRemote():
    fail("Not supported")

def setConnection(name=None, device=None):
    dict = get_instance("name", name)
    if dict and dict.has_key("device"):
        notify("Net.Link.connectionChanged", "configured " + name)
    else:
        notify("Net.Link.connectionChanged", "added " + name)

def deleteConnection(name=None):
    dev = Dev(name)
    if dev.ifc and dev.state == "up":
        dev.down()
    notify("Net.Link.connectionChanged", "deleted " + name)

def setAddress(name=None, mode=None, address=None, mask=None, gateway=None):
    dev = Dev(name)
    if dev.state == "up":
        dev.address = address
        dev.gateway = gateway
        dev.up()
    notify("Net.Link.connectionChanged", "configured " + name)

def setRemote(name=None, remote=None):
    fail("Not supported")

def setNameService(name=None, namemode=None, nameserver=None):
    if not namemode in ("default", "auto", "custom"):
        fail("invalid namemode")
    notify("Net.Link.connectionChanged", "configured " + name)

def setState(name=None, state=None):
    dev = Dev(name)
    if state != "up" and state != "down":
        fail("unknown state")
    
    if not dev.ifc:
        return
    
    if state == "up":
        stopSameDev(name, dev.uid)
        dev.up()
    else:
        if dev.state == "up":
            dev.down()

def connections():
    list = instances("name")
    if list:
        return "\n".join(list)
    return ""

def connectionInfo(name=None):
    dev = Dev(name, True)
    s = "name=%s" % name
    if dev.uid:
        s += "\ndevice_id=%s\ndevice_name=%s" % (dev.uid, network.deviceName(dev.uid))
    s += "\nnet_mode=%s" % dev.mode
    if dev.address:
        s += "\nnet_address=%s" % dev.address
    if dev.mask:
        s += "\nnet_mask=%s" % dev.mask
    if dev.gateway:
        s += "\nnet_gateway=%s" % dev.gateway
    s += "\nnamemode=%s" % dev.namemode
    if dev.nameserver:
        s += "\nnameserver=%s" % dev.nameserver
    if dev.state == "up":
        if dev.ifc:
            if dev.mode == "auto":
                if dev.ifc.isAuto() and dev.ifc.isUp():
                    state = "up " + dev.ifc.getAddress()[0]
                else:
                    state = "inaccessible " + _(dhcp_fail_msg)
            else:
                if dev.ifc.isUp():
                    state = "up " + dev.ifc.getAddress()[0]
                else:
                    state = "down"
        else:
            state = "inaccessible " + _(no_device_msg)
    else:
        if dev.ifc:
            state = "down"
        else:
            state = "unavailable"
    s += "\nstate=%s" % state
    return s
