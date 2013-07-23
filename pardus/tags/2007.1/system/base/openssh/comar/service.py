from comar.service import *
import os

def check_config():
    if not os.path.exists("/etc/ssh/sshd_config"):
        fail("You need /etc/ssh/sshd_config to run sshd")

    if not os.path.exists("/etc/ssh/ssh_host_key"):
        run("/usr/bin/ssh-keygen", "-t", "rsa1", "-b", "1024",
            "-f", "/etc/ssh/ssh_host_key", "-N", "")

    if not os.path.exists("/etc/ssh/ssh_host_dsa_key"):
        run("/usr/bin/ssh-keygen", "-d", "-f",
            "/etc/ssh/ssh_host_dsa_key", "-N", "")

    if not os.path.exists("/etc/ssh/ssh_host_rsa_key"):
        run("/usr/bin/ssh-keygen", "-t", "rsa",
            "-f", "/etc/ssh/ssh_host_rsa_key", "-N", "")

serviceType = "server"
serviceDesc = _({"en": "Secure Shell Server",
                 "tr": "Güvenli Kabuk Sunucusu"})

def start():
    check_config()
    ret = run("/sbin/start-stop-daemon", "--start", "--quiet",
              "--pidfile", "/var/run/sshd.pid",
              "--startas", "/usr/sbin/sshd")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/sshd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/sshd.pid")
