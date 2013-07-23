#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbus

WPAS_DBUS_OPATH = "/fi/epitest/hostap/WPASupplicant"
WPAS_DBUS_INTERFACES_OPATH = "/fi/epitest/hostap/WPASupplicant/Interfaces"

WPAS_DBUS_SERVICE = "fi.epitest.hostap.WPASupplicant"
WPAS_DBUS_INTERFACE = "fi.epitest.hostap.WPASupplicant"
WPAS_DBUS_INTERFACES_INTERFACE = "fi.epitest.hostap.WPASupplicant.Interface"
WPAS_DBUS_NETWORK_INTERFACE = "fi.epitest.hostap.WPASupplicant.Network"
WPAS_DBUS_BSSID_INTERFACE = "fi.epitest.hostap.WPASupplicant.BSSID"

class PasswordLengthError(Exception):
    pass

class WPA_Supplicant_Network:
    def __init__(self, bus, path):
        self.bus = bus
        self.path = path
        self.net_obj = self.bus.get_object(WPAS_DBUS_SERVICE, path)
        self.net = dbus.Interface(self.net_obj, WPAS_DBUS_NETWORK_INTERFACE)

    # dict keys: ssid, bssid, key_mgmt, psk, scan_ssid, pairwise, group, eap, identity,
    # anonymous_identity, ca_cert, ca_cert2, client_cert, client_cert2, private_key, private_key2,
    # private_key_passwd, private_key2_passwd, phase1, phase2, eapol_flags
    #
    # Example: setNetwork({"ssid":dbus.String("MySSID", variant_level=1)),
    # "psk":dbus.String("MyPassword", variant_level=1))})
    def setNetwork(self, options):
        self.net.set(options)

    def enableNetwork(self):
        self.net.enable()

    def disableNetwork(self):
        self.net.disable()

class WPA_Supplicant_Interface:
    def __init__(self, bus, ifname, path):
        self.bus = bus
        self.ifname = ifname
        self.path = path
        self.if_obj = self.bus.get_object(WPAS_DBUS_SERVICE, path)
        self.iface = dbus.Interface(self. if_obj, WPAS_DBUS_INTERFACES_INTERFACE)

    def scan(self):
        self.iface.scan()

    def scanResults(self):
        return self.iface.scanResults()

    def addNetwork(self):
        path = self.iface.addNetwork()
        return self.getNetwork(path)

    def removeNetwork(self, network):
        self.iface.removeNetwork(network)

    def selectNetwork(self, network):
        self.iface.selectNetwork(network)

    def getNetworkPath(self, network_id):
        return "%s/Networks/%d" % (self.path, network_id)

    def getNetworkById(self, network_id):
        return WPA_Supplicant_Network(self.bus, self.getNetworkPath(network_id))

    def getNetwork(self, network):
        return WPA_Supplicant_Network(self.bus, network)

    # mode should be between 0 and 2
    def setAPScan(self, mode):
        self.iface.setAPScan(dbus.UInt32(mode))

    def disconnect(self):
        self.iface.disconnect()

    def getState(self):
        return self.iface.state()

    def getCapabilities(self):
        return self.iface.capabilities()

class WPA_Supplicant:
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.wpas_obj = self.bus.get_object(WPAS_DBUS_SERVICE, WPAS_DBUS_OPATH)
        self.wpas = dbus.Interface(self.wpas_obj, WPAS_DBUS_INTERFACE)

    def getInterface(self, ifname):
        path = self.wpas.getInterface(ifname)
        return WPA_Supplicant_Interface(self.bus, ifname, path)

    # driver=wext, hostap, prism54, madwifi, atmel, ndiswrapper, ipw, wired
    def addInterface(self, ifname, driver):
        self.wpas.addInterface(ifname, {'driver': dbus.String(driver, variant_level=1)})
        return self.getInterface(ifname)

    def removeInterface(self, ifname):
        try:
            iface_path = self.wpas.getInterface(ifname)
        except dbus.DBusException:
            iface_path = None
        if iface_path:
            self.wpas.removeInterface(dbus.ObjectPath(iface_path))

def detectWpaDriver(ifname):
    import os
    import sys
    import comar.network
    # if device is an ethernet device, driver is "wired"
    device = comar.network.IF(ifname)
    if (device.isEthernet()) and (not device.isWireless()):
        return "wired"
    path = os.path.join("/sys/class/net/", ifname, "device/driver/module")
    modname = None
    if os.path.exists(path):
        modname = os.readlink(path).split("/")[-1]
        if "hostap" in modname:
            return "hostap"
        if "prism54" in modname:
            return "prism54"
        if "ndiswrapper" in modname:
            return "ndiswrapper"
        if "atmel" in modname:
            return "atmel"
        if "madwifi" in modname:
            return "madwifi"
    # we fallback to wext
    # wext is the generic driver
    return "wext"

def getWpaInterface(ifname):
    wpa = WPA_Supplicant()
    try:
        iface = wpa.getInterface(ifname)
    except dbus.DBusException:
        driver = detectWpaDriver(ifname)
        iface = wpa.addInterface(ifname, driver)
    return iface

def waitForAuthenticationComplete(iface, timeout, wait = 0.1):
    import time
    while timeout > 0:
        if iface.getState() == "COMPLETED":
            return True
        else:
            timeout -= wait
        time.sleep(wait)
    return False

import comar

def checkServiceState(serviceName):
    com = comar.Link()
    com.call_package("System.Service.info", serviceName)
    state = com.read_cmd()[2].split("\n")[1]
    return state in ("on", "started")

def startService(serviceName):
    com = comar.Link()
    com.call_package("System.Service.start", serviceName)
    return com.read_cmd()[0] == com.RESULT

def isDBusServiceActive():
    return checkServiceState("dbus")

def isWpaServiceActive():
    return checkServiceState("wpa_supplicant")

def isWpaServiceUsable():
    return isDBusServiceActive() and isWpaServiceActive()

def startWpaService():
    dbus_state = True
    wpa_state = True
    # we need DBus service
    if not isDBusServiceActive():
        dbus_state = startService("dbus")
    if not isWpaServiceActive():
        wpa_state = startService("wpa_supplicant")
    return dbus_state and wpa_state

def setWpaAuthentication(ifname, ssid, password, timeout = 10):
    password_length = len(password)
    if (password_length < 8) or (password_length > 63):
        raise PasswordLengthError("Password length should be between 8 and 63")
    iface = getWpaInterface(ifname)
    network = iface.addNetwork()
    network.setNetwork({"ssid": dbus.String(ssid, variant_level=1), "psk": dbus.String(password, variant_level=1)})
    iface.selectNetwork(network.path)
    authentication = waitForAuthenticationComplete(iface, timeout)
    if not authentication:
        disableAuthentication(ifname)
    return authentication

def disableAuthentication(ifname):
    wpa = WPA_Supplicant()
    wpa.removeInterface(ifname)
