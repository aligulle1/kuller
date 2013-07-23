#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

name_msg = {
    "en": "Dialup network",
    "tr": "Çevirmeli ağlar"
}

remote_name_msg = {
    "en": "Phone number",
    "tr": "Telefon numarası"
}

# Silly modem device list :/
# Appearently checking existance of these devices is easiest way to detect modems
modem_devices = (
    # Standart list
    "/dev/modem",
    "/dev/ttyS0",
    "/dev/ttyS1",
    "/dev/ttyS2",
    "/dev/ttyS3",
    "/dev/ttyS4",
    # ISDN
    "/dev/ttyI0",
    "/dev/ttyI1",
    "/dev/ttyI2",
    "/dev/ttyI3",
    # USB
    "/dev/usb/ttyACM0",
    "/dev/usb/ttyACM1",
    "/dev/usb/ttyACM2",
    "/dev/usb/ttyACM3",
    "/dev/usb/ttyUSB0",
    "/dev/usb/ttyUSB1",
    "/dev/usb/ttyUSB2",
    "/dev/usb/ttyUSB3",
    "/dev/ttyACM0",
    "/dev/ttyACM1",
    "/dev/ttyACM2",
    "/dev/ttyACM3",
    "/dev/ttyUSB0",
    "/dev/ttyUSB1",
    "/dev/ttyUSB2",
    "/dev/ttyUSB3",
    # BlueTooth
    "/dev/rfcomm0",
    "/dev/rfcomm1",
    "/dev/rfcomm2",
    "/dev/rfcomm3",
    # IrDA
    "/dev/ircomm0",
    "/dev/ircomm1",
    "/dev/ircomm2",
    "/dev/ircomm3",
    # slmodem
    "/dev/ttySL0",
    "/dev/ttySL1",
    "/dev/ttySL2",
    "/dev/ttySL3",
    # hsfmodem
    "/dev/ttySHSF0",
    "/dev/ttySHSF1",
    "/dev/ttySHSF2",
    "/dev/ttySHSF3",
    # hcfmodem
    "/dev/ttySHCF0",
    "/dev/ttySHCF1",
    "/dev/ttySHCF2",
    "/dev/ttySHCF3",
    # ltmodem
    "/dev/ttyLTM0",
    "/dev/ttyLTM1",
    "/dev/ttyLTM2",
    "/dev/ttyLTM3",
)

import os
import popen2
from csapi import atoi
from signal import SIGTERM


class Dialup:
    """ Dialup client functions for Hayes compatible modems, using pppd """

    tmpl_chat = """
TIMEOUT         5
ABORT           '\\nBUSY\\r'
ABORT           '\\nNO ANSWER\\r'
ABORT           '\\nNO CARRIER\\r'
ABORT           '\\nNO DIALTONE\\r'
ABORT           '\\nAccess denied\\r'
ABORT           '\\nInvalid\\r'
ABORT           '\\nVOICE\\r'
ABORT           '\\nRINGING\\r\\n\\r\\nRINGING\\r'
''              \\rAT
'OK-+++\c-OK'   ATH0
TIMEOUT         30
OK              ATL%s
OK              ATDT%s
CONNECT         ''
"""
    
    tmpl_options = """
lock
modem
crtscts
noipdefault
defaultroute
noauth
usehostname
usepeerdns
linkname %s
user %s
%s
"""

    def silentUnlink(self, path):
        """ Try to unlink a file, if exists """

        try:
            os.unlink(path)
        except:
            pass

    def capture(self, cmd):
        """ Run a command and capture the output """

        out = []
        a = popen2.Popen4(cmd)
        while 1:
            b = a.fromchild.readline()
            if b == None or b == "":
                break
            out.append(b)
        return (a.wait(), out)

    def sendCmd(self, cmd, dev):
        """ Send commands to dev """

        return result

    def isModem(self, dev):
        """ Check if dev is a modem """
        
        return True

    def getDNS(self):
        """ Try to get DNS server adress provided by remote peer """

        list = []
        try:
            f = file("/etc/ppp/resolv.conf", "r")
            for line in f.readlines():
                if line.strip().startswith("nameserver"):
                    list.append(line[line.find("nameserver") + 10:].rstrip('\n').strip())
            f.close()
        except IOError:
            return None

        return list

    def createOptions(self, dev, user, speed):
        """ Create options file for the desired device """

        self.silentUnlink("/etc/ppp/options." + dev)
        try:
            f = open("/etc/ppp/options." + dev, "w")
            f.write(self.tmpl_options % (dev, user, speed))
            f.close()
        except:
            return True

        return None

    def createChatscript(self, dev, phone, vol):
        """ Create a script to have a chat with the modem in the frame of respect and love """

        self.silentUnlink("/etc/ppp/chatscript." + dev)
        try:
            f = open("/etc/ppp/chatscript." + dev, "w")
            f.write(self.tmpl_chat % (vol, phone))
            f.close()
        except:
            return True

        return None


    def createSecrets(self, user, pwd):
        """ Create authentication files """

        try:
            # Ugly way to clean up secrets and recreate
            self.silentUnlink("/etc/ppp/pap-secrets")
            self.silentUnlink("/etc/ppp/chap-secrets")
            f = os.open("/etc/ppp/pap-secrets", os.O_CREAT, 0600)
            os.close(f)
            os.symlink("/etc/ppp/pap-secrets", "/etc/ppp/chap-secrets")
        except:
            return True
            
        f = open("/etc/ppp/pap-secrets", "w")
        data = "\"%s\" * \"%s\"\n" % (user, pwd)
        f.write(data)
        f.close()

        return None

    def stopPPPD(self, dev):
        """ Stop the connection and hangup the modem """

        try:
            f = open("/var/lock/LCK.." + dev, "r")
            pid = atoi(f.readline())
            f.close()
        except:
            return "Could not open lockfile"

        try:
            os.kill(pid, SIGTERM)
        except OSError:
            return "Could not stop the process"

        return "Killed"

    def runPPPD(self, dev):
        """ Run the PPP daemon """

        # PPPD does some isatty and ttyname checks, so we shall satisfy it for symlinks and softmodems
        cmd = "/usr/sbin/pppd /dev/" + dev + " connect '/usr/sbin/chat -V -v -f /etc/ppp/chatscript." + dev + "'"
        i, output = self.capture(cmd)

        return output

    def dial(self, phone, user, pwd, speed, vol, modem = "modem"):
        """ Dial a server and try to login """
    
        dev = modem.lstrip("/dev/")

        if self.createSecrets(user, pwd) is True:
            return "Could not manage authentication files"

        if self.createOptions(dev, user, speed) is True:
            return "Could not manage pppd parameters"

        if self.createChatscript(dev, phone, vol) is True:
            return "Could not manage chat script"

        output = self.runPPPD(dev)
        return output


def _device_dev(uid):
    return uid[uid.find(":") + 1:]

def _device_info(uid):
    return uid[uid.find(":") + 1:]

def _get(dict, key, default):
    val = default
    if dict and dict.has_key(key):
        val = dict[key]
    return val


class Dev:
    def __init__(self, name, want=False):
        dict = get_instance("name", name)
        if want:
            if not dict:
                fail("No such connection")
        self.uid = _get(dict, "device", None)
        self.name = name
        self.dev = None
        if self.uid:
            self.dev = _device_dev(self.uid)
        self.state = _get(dict, "state", "down")
        self.remote = _get(dict, "remote", None)
        self.authmode = _get(dict, "authmode", "none")
        self.user = _get(dict, "user", None)
        self.password = _get(dict, "password", None)
    
    def up(self):
        dial = Dialup()
        
        if self.remote and self.user and self.password and self.dev:
            notify("Net.Link.stateChanged", self.name + "\nconnecting")
            
            dial.dial(self.remote, self.user, self.password, "115200", "1", self.dev)
            
            notify("Net.Link.stateChanged", self.name + "\nup")
    
    def down(self):
        dial = Dialup()
        dial.stopPPPD(self.dev)
        notify("Net.Link.stateChanged", self.name + "\ndown")


#

def linkInfo():
    return """type=dialup
name=%s
modes=device,remote,auth
auth_modes=login,login,Login
remote_name=%s""" % (_(name_msg), _(remote_name_msg))

def deviceList():
    iflist = []
    for dev in modem_devices:
        if os.path.exists(dev):
            iflist.append("modem:%s %s" % (dev, _device_info(dev)))
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
    if dev.dev and dev.state == "up":
        dev.down()
    notify("Net.Link.connectionChanged", "deleted " + name)

def setAddress(name=None, mode=None, address=None, mask=None, gateway=None):
    fail("Not supported")

def setRemote(name=None, remote=None):
    notify("Net.Link.connectionChanged", "configured " + name)

def setAuthentication(name=None, authmode=None, user=None, password=None, key=None):
    notify("Net.Link.connectionChanged", "configured " + name)

def setState(name=None, state=None):
    dev = Dev(name)
    if state != "up" and state != "down":
        fail("Unknown state")
    
    if not dev.dev:
        fail("Device not found")
    
    if state == "up":
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
        s += "\ndevice_id=%s\ndevice_name=%s" % (dev.uid, _device_info(dev.uid))
    if dev.remote:
        s += "\nremote=%s" % dev.remote
    # FIXME:
    state = dev.state
    s += "\nstate=%s" % state
    return s

def getAuthentication(name=None):
    dev = Dev(name)
    return "%s\n%s\n%s\n%s" % (name, dev.authmode, dev.user, dev.password)
