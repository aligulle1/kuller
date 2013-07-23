from comar.service import *
import os
import time

serviceType = "script"
serviceConf = "bluetooth"
serviceDesc = _({"en": "Bluetooth Utils",
                 "tr": "Bluetooth Araçları"})

def start():
    config = loadConfig()

    cfg = lambda x, xx="false": config.get(x, xx)
    cfg_exists = lambda x: x in config and os.access(config[x], os.F_OK)

    if cfg("HID2HCI_ENABLE") == "true":
        run("/usr/sbin/hid2hci -0 -q")
        time.sleep(1)

    if cfg("HCID_ENABLE") == "true" and cfg_exists("HCID_CONFIG"):
        run("/sbin/start-stop-daemon --start --quiet \
                     --exec /usr/sbin/hcid -- -f %s" % cfg("HCID_CONFIG", ""))

    if cfg("SDPD_ENABLE") == "true":
        run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/sdpd")

    if cfg("HIDD_ENABLE") == "true":
        run("/sbin/start-stop-daemon --start --quiet \
             --exec /usr/bin/hidd -- %s --server" % cfg("HIDD_OPTIONS", ""))

    if cfg("RFCOMM_ENABLE") == "true" and cfg_exists("RFCOMM_CONFIG"):
        run("/usr/bin/rfcomm -f %s bind all" % config["RFCOMM_CONFIG"])

    if cfg("DUND_ENABLE") == "true" and "DUND_OPTIONS" in config:
        run("/sbin/start-stop-daemon --start --quiet \
             --exec /usr/bin/dund -- %s" % cfg("DUND_OPTIONS", ""))

    if cfg("PAND_ENABLE") == "true":
        run("/sbin/start-stop-daemon --start --quiet \
             --exec /usr/bin/pand -- %s" % cfg("PAND_OPTIONS", ""))

    if os.access("/etc/bluetooth/uart", os.F_OK):
        uart_conf = [i[:-1] for i in open("test") if re.match("^[^#]", i)]
        for i in uart_conf:
            run("/usr/sbin/hciattach %s" % i)

    if cfg("DISCOVERABLE") == "true":
        run("/usr/bin/dbus-send --system --dest=org.bluez /org/bluez/hci0 org.bluez.Adapter.SetDiscoverableTimeout uint32:0")
        run("/usr/bin/dbus-send --system --dest=org.bluez /org/bluez/hci0 org.bluez.Adapter.SetMode string:discoverable")

    run("/sbin/start-stop-daemon --start --quiet --background --make-pidfile --pidfile /var/run/passkey.pid --exec /usr/bin/passkey-agent -- --default /etc/bluetooth/pin-helper")
    notify("System.Service.changed", "started")

def stop():
    config = loadConfig()

    cfg = lambda x, xx="false": config.get(x, xx)

    if cfg("PAND_ENABLE") == "true":
        run("/sbin/start-stop-daemon --stop --quiet --exec /usr/bin/pand")

    if cfg("DUND_ENABLE") == "true":
        run("/sbin/start-stop-daemon --stop --quiet --exec /usr/bin/dund")

    if cfg("RFCOMM_ENABLE") == "true":
        run("/usr/bin/rfcomm release all")

    if cfg("HIDD_ENABLE") == "true":
        run("/sbin/start-stop-daemon --stop --quiet --exec /usr/bin/hidd")

    if cfg("SDPD_ENABLE") == "true":
        run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/sdpd")

    if cfg("HCID_ENABLE") == "true":
        run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/hcid")

    run("/usr/bin/killall hciattach")
    run("/sbin/start-stop-daemon --stop --quiet --exec /usr/bin/passkey-agent --p /var/run/passkey.pid")

    notify("System.Service.changed", "stopped")

def status():
    return checkDaemon("/var/run/passkey.pid")
