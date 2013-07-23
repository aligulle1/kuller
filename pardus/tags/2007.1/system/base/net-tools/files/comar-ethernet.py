#!/usr/bin/python

import os
from comar import network

action = os.environ.get("ACTION", None)
devpath = os.environ.get("DEVPATH", None)

if action == "add":
    ifc = network.IF(devpath.split("/")[-1])
    if not ifc.isWireless():
        os.system('/usr/bin/hav event Net.Link kernelEvent net-tools "add@%s"' % devpath)
elif action == "remove":
    #FIXME: need to keep some state about add events, or we cant get actual
    #connection name or device type
    pass

