#!/usr/bin/python
#-*- coding: UTF-8 -*-

from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "Gnome Display Manager",
    "tr": "Gnome Görüntü Yöneticisi",
})

def loadLang():
    locale = open("/etc/env.d/03locale").read().split("=")[2].rstrip("\n")
    os.environ['LC_ALL'] = locale

def start():
    call("System.Service.start", "acpid")
    call("System.Service.start", "hal")
    
    loadLang()
    run("/usr/sbin/gdm-binary")
    notify("System.Service.changed", "started")

def stop():
    run("/usr/sbin/gdm-stop")
    notify("System.Service.changed", "stopped")

def status():
    return checkDaemon("/var/run/gdm.pid")
