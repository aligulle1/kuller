from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "Custom startup commands",
    "tr": "Kullanıcı başlangıç komutları"
})
serviceDefault = "on"

def start():
    if os.path.exists("/etc/conf.d/local.start"):
        os.system("source /etc/conf.d/local.start")
    notify("System.Service.changed", "started")

def stop():
    if os.path.exists("/etc/conf.d/local.stop"):
        os.system("source /etc/conf.d/local.stop")
    notify("System.Service.changed", "stopped")
