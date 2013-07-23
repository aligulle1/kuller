from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Dazuko kernel module",
                 "tr": "Dazuko çekirdek modülü"})

dazuko_dev = '/dev/dazuko'

def start():
    if run("/sbin/modprobe dazuko") != 0:
        fail("cannot load dazuko module")
    if run("/sbin/modprobe capability") != 0:
        fail("cannot load capability module")

def stop():
    if run("/sbin/modprobe -r dazuko") != 0:
        fail("cannot remove dazuko module")

def status():
    return os.access(dazuko_dev, os.F_OK)
