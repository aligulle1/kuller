from comar.service import *
import signal

serviceType = "local"
serviceDesc = _({"en": "uShare UPnP A/V Media Server",
                 "tr": "uShare UPnP Ses/Görüntü Ortam Sunucu"})
serviceDefault = "off"

pid_file = "/var/run/ushare.pid"
command = "/usr/bin/ushare"
conf_file = "/etc/ushare.conf"

def check_ushare_dir():
    conf = open(conf_file)

    for line in conf.readlines():
        line = line.strip()
        if line.startswith("USHARE_DIR"):
            ushare_dir = line.split("=")[1]

    conf.close()

    if not os.path.exists(ushare_dir):
        fail('uShare directory "%s" doesn\'t exist, please edit %s and set a valid directory.' % (ushare_dir, conf_file))

@synchronized
def start():
    check_ushare_dir()
    startService(command=command,
                 args="--cfg=/etc/ushare.conf -d",
                 pidfile=pid_file,
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pid_file,
                donotify=True)

def reload():
    stopService(command=command,
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(pid_file)
