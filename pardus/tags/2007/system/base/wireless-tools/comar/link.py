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
    "en": "Wireless network",
    "tr": "Kablosuz ağlar"
}

dhcp_fail_msg = {
    "en": "Could not get address",
    "tr": "Adres alınamadı"
}

no_device_msg = {
    "en": "Device is not plugged",
    "tr": "Aygıt takılı değil"
}

wpa_psp_msg = {
    "en": "WPA PreShared Passphrase",
    "tr": "WPA Ortak Parola"
}

import os
import re
import socket
import array
import struct
import fcntl
import subprocess
from comar import network

# From </usr/include/wireless.h>
SIOCSIWMODE = 0x8B06    # set the operation mode
SIOCGIWMODE = 0x8B07    # get operation mode
SIOCGIWRATE = 0x8B21    # get default bit rate
SIOCSIWESSID = 0x8B1A   # set essid
SIOCGIWESSID = 0x8B1B   # get essid


class Point:
    def __init__(self, id=None):
        self.ssid = None
        self.mode = None
        self.mac = None
        if id:
            if " (" in id and id.endswith(")"):
                self.ssid, rest = id.split(" (", 1)
                self.mode, self.mac = rest.split(" ", 1)
                self.mac = self.mac[:-1]
            else:
                self.ssid = id
    
    def id(self):
        return "%s (%s, %s)" % (self.ssid, self.mode, self.mac)


class Wireless:
    modes = ['Auto', 'Ad-Hoc', 'Managed', 'Master', 'Repeat', 'Second', 'Monitor']
    
    def __init__(self, ifc):
        self.sock = None
        self.ifc = ifc
    
    def _call(self, func, arg = None):
        if arg is None:
            data = (self.ifc.name + '\0' * 32)[:32]
        else:
            data = (self.ifc.name + '\0' * 16)[:16] + arg
        try:
            result = self.ifc.ioctl(func, data)
        except IOError:
            return None
        return result
    
    def getSSID(self):
        buffer = array.array('c', '\0' * 16)
        addr, length = buffer.buffer_info()
        arg = struct.pack('Pi', addr, length)
        self._call(SIOCGIWESSID, arg)
        return buffer.tostring().strip('\x00')
    
    def setSSID(self, ssid):
        point = Point(ssid)
        buffer = array.array('c', point.ssid + '\x00')
        addr, length = buffer.buffer_info()
        arg = struct.pack("iHH", addr, length, 1)
        self._call(SIOCSIWESSID, arg)
        if self.getSSID() is point.ssid:
            return True
        else:
            return None
    
    def scanSSID(self):
        ifc = self.ifc
        if not ifc.isUp():
            # Some drivers cant do the scan while interface is down, doh :(
            ifc.setAddress("0.0.0.0")
            ifc.up()
        cmd = subprocess.Popen(["/usr/sbin/iwlist", ifc.name, "scan"], stdout=subprocess.PIPE)
        data = cmd.communicate()[0]
        points = []
        point = None
        for line in data.split("\n"):
            line = line.lstrip()
            if line.startswith("Cell "):
                if point != None:
                    points.append(point)
                point = Point()
            if "ESSID:" in line:
                i = line.find('"') + 1
                j = line.find('"', i)
                point.ssid = line[i:j]
            if "Mode:" in line:
                point.mode = line.split("Mode:")[1]
            if "Address:" in line:
                point.mac = line.split("Address:")[1].strip()
        if point != None:
            points.append(point)
        return points
    
    def getMode(self):
        result = self._call(SIOCGIWMODE)
        mode = struct.unpack("i", result[16:20])[0]
        return self.modes[mode]
    
    def setMode(self, mode):
        arg = struct.pack("l", self.modes.index(mode))
        self._call(SIOCSIWMODE, arg)
        if self.getMode() is mode:
            return True
        else:
            return None
    
    def setEncryption(self, mode="none", password=None):
        ifc = self.ifc
        if mode and mode != "" and mode != "none":
            if mode == "wep":
                os.system("/usr/sbin/iwconfig '%s' enc restricted '%s'" % (ifc.name, password))
            elif mode == "wepascii":
                os.system("/usr/sbin/iwconfig '%s' enc restricted 's:%s'" % (ifc.name, password))
            elif mode == "wpa-psp":
                # FIXME: wpa code, not finished yet
                pidfile = "/var/run/wpa_supplicant_%s.pid" % ifc.name
                conffile = "/var/run/wpa_supplicant_%s.conf" % ifc.name
                # FIXME: setup conf file with wpa_passphrase here
                subprocess.call([
                    "/sbin/start-stop-daemon",
                    "--start",
                    "--pidfile",
                    pidfile,
                    "--exec",
                    "/usr/sbin/wpa_supplicant",
                    "--",
                    "-B",
                    "-P",
                    pidfile,
                    "-i",
                    ifc.name,
                    "-w",
                    "-c",
                    conffile
                ])
        else:
            os.system("/usr/sbin/iwconfig %s enc off" % (ifc.name))
            return
            # FIXME: wpa code, not finished yet
            pidfile = "/var/run/wpa_supplicant_%s.pid" % ifc.name
            subprocess.call([
                "/sbin/start-stop-daemon",
                "--stop",
                "--pidfile",
                pidfile,
                "--exec",
                "/usr/sbin/wpa_supplicant"
            ])
    
    def getBitrate(self, ifname):
        # Note for UI coder, KILO is not 2^10 in wireless tools world
        result = self._call(SIOCGIWRATE)
        size = struct.calcsize('ihbb')
        m, e, i, pad = struct.unpack('ihbb', result[16:16+size])
        if e == 0:
            bitrate =  m
        else:
            bitrate = float(m) * 10**e
        return bitrate
    def getLinkStatus(self, ifname):
        """ Get link status of an interface """
        link = self._readsys(ifname, "wireless/link")
        return int(link)
    def getNoiseStatus(self, ifname):
        """ Get noise level of an interface """
        noise = self._readsys(ifname, "wireless/noise")
        return int(noise) - 256
    def getSignalStatus(self, ifname):
        """ Get signal status of an interface """
        signal = self._readsys(ifname, "wireless/level")
        return int(signal) - 256


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
        self.remote = _get(dict, "remote", None)
        self.mode = _get(dict, "mode", "auto")
        self.address = _get(dict, "address", None)
        self.mask = _get(dict, "mask", None)
        self.gateway = _get(dict, "gateway", None)
        self.authmode = _get(dict, "authmode", "none")
        self.password = _get(dict, "password", "")
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
        wifi = Wireless(ifc)
        wifi.setEncryption(mode=self.authmode, password=self.password)
        if self.remote:
            wifi.setSSID(self.remote)
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
        wifi = Wireless(ifc)
        if self.mode != "manual":
            ifc.stopAuto()
        if self.authmode != "" and self.authmode != "none":
            wifi.setEncryption("none", None)
        ifc.down()
        notify("Net.Link.stateChanged", self.name + "\ndown")


# Net.Link API

def kernelEvent(data):
    type, dir = data.split("@", 1)
    if not dir.startswith("/class/net/"):
        return
    devname = dir[11:]
    flag = 1
    
    ifc = network.IF(devname)
    if type == "add":
        if not ifc.isWireless():
            return
        devuid = ifc.deviceUID()
        notify("Net.Link.deviceChanged", "added wifi %s %s" % (devuid, network.deviceName(devuid)))
        conns = instances("name")
        for conn in conns:
            dev = Dev(conn)
            if dev.ifc and dev.ifc.name == devname:
                if dev.state == "up":
                    dev.up()
                    return
                flag = 0
        if flag:
            notify("Net.Link.deviceChanged", "new wifi %s %s" % (devuid, network.deviceName(devuid)))
    
    elif type == "remove":
        conns = instances("name")
        for conn in conns:
            dev = Dev(conn)
            # FIXME: ifc is not enough here :(
            if dev.ifc and dev.ifc.name == devname:
                if dev.state == "up":
                    notify("Net.Link.stateChanged", dev.name + "\ninaccessible " + "Device removed")
        notify("Net.Link.deviceChanged", "removed wifi %s" % devname)

def linkInfo():
    return """type=wifi
modes=device,remote,scan,net,auto,auth
auth_modes=wep,pass,WEP;wepascii,pass,WEP ASCII
name=%s
remote_name=ESS ID""" % _(name_msg)
#;wpa-psp,pass,%s
#(_(wpa_psp_msg), )

def deviceList():
    iflist = []
    for ifc in network.interfaces():
        if ifc.isWireless():
            uid = ifc.deviceUID()
            info = network.deviceName(uid)
            iflist.append("%s %s" % (uid, info))
    return "\n".join(iflist)

def scanRemote(device=None):
    if device:
        ifc = network.findInterface(device)
        if ifc:
            wifi = Wireless(ifc)
            points = map(lambda x: x.id(), wifi.scanSSID())
            return "\n".join(points)
    return ""

def setConnection(name=None, device=None):
    dict = get_instance("name", name)
    if dict and dict.has_key("device"):
        notify("Net.Link.connectionChanged", "configured " + name)
    else:
        notify("Net.Link.connectionChanged", "added " + name)

def deleteConnection(name=None):
    dev = Dev(name, True)
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
    notify("Net.Link.connectionChanged", "configured " + name)

def setAuthentication(name=None, authmode=None, user=None, password=None, key=None):
    notify("Net.Link.connectionChanged", "configured " + name)

def setNameService(name=None, namemode=None, nameserver=None):
    if not namemode in ("default", "auto", "custom"):
        fail("invalid namemode")
    notify("Net.Link.connectionChanged", "configured " + name)

def setState(name=None, state=None):
    dev = Dev(name)
    if state != "up" and state != "down":
        fail("unknown state")
    
    if not dev.ifc:
        fail("Device not found")
    
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
    if dev.remote:
        s += "\nremote=%s" % dev.remote
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
            state = "inaccessible " + _(no_device_msg)
    else:
        if dev.ifc:
            state = "down"
        else:
            state = "unavailable"
    s += "\nstate=%s" % state
    return s

def getAuthentication(name=None):
    dev = Dev(name, True)
    return "%s\n%s\n%s" % (name, dev.authmode, dev.password)
