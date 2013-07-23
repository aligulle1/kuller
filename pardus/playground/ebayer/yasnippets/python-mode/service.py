# name: service.py template
# key: service
# binding: direct-keybinding
# --
#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "$1",
                 "tr": "$2"})

from comar.service import *

@synchronized
def start():
${3:pass}

@synchronized
def stop():
${4:pass}

def status():
    return isServiceRunning("$5")
