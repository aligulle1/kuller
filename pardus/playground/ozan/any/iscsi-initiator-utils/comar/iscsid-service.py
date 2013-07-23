from comar.service import *

import os

serviceType = "local"
serviceDesc = _({"en": "iSCSI daemon",
                 "tr": "iSCSI hizmeti"})

MSG_WONTSTART = _({"en": "Nodes are not configured to start automatically or rootfs is not on iSCSI",
                   "tr": "Düğümler otomatik başlayacak şekilde ayarlanmamış veya kök dosya sistemi iSCSI üzerinde değil",
                   })

ISCSID = "/sbin/iscsid"
PID_FILE = "/var/run/iscsid.pid"
ISCSI_DIR = "/var/lib/iscsi"

def root_is_on_iscsi():
    # Check whether the root partition is on iSCSI
    # FIXME: This has a false positive if root is on nfs
    retval = False
    for line in open("/proc/mounts", "r").read().strip().split("\n"):
        if line.split()[1] == "/" and "rootfs" not in line:
            retval = "_netdev" in line.split()[3]
    return retval


@synchronized
def start():
    # Only start if nodes are setup to startup automatically,root is iSCSI
    # or if iscsid is managing the sessions.
    if os.system('grep -qrs "node.startup = automatic" %s/nodes' \
            % ISCSI_DIR) == 0 or \
            root_is_on_iscsi() or \
            use_discoveryd():

        # Load kernel modules
        for mod in ("iscsi_tcp", "ib_iser", "cxgb3i",
                    "bnx2i", "be2iscsi"):
            os.system("modprobe -q %s" % mod)

        startService(command=ISCSID,
                     pidfile=PID_FILE,
                     detach=True,
                     makepid=True,
                     donotify=True)
    else:
        fail(MSG_WONTSTART)

@synchronized
def stop():
    # Remove drivers
    os.system("modprobe -rq ib_iser")
    os.system("modprobe -rq iscsi_tcp")

    stopService(command=ISCSID,
                donotify=True)

def status():
    return isServiceRunning(command=ISCSID)
