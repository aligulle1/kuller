from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Ejabberd Jabber Server",
                 "tr": "Ejabberd Jabber Sunucusu"})

@synchronized
def start():
    loadEnvironment()

    # Use more than 1024 connections... (~6MB more memory will be used)
    os.environ["ERL_MAX_PORTS"] = "32000"
    os.environ["HOME"] = "/usr/var/lib/ejabberd/"

    startService(command="/usr/bin/erl",
                 args="-pa /usr/lib/erlang/lib/ejabberd-2.0.1/ebin \
                       -sname ejabberd \
                       -s ejabberd \
                       -ejabberd config \"/etc/jabber/ejabberd.cfg\" \
                                 log_path \"/var/log/jabber/ejabberd.log\" \
                       -mnesia dir \"/var/lib/jabber/spool\" \
                       -kernel inetrc \"/etc/jabber/inetrc\" \
                       -detached",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ejabberdctl",
                args="--node ejabberd@localhost stop",
                donotify=True)

def ready():
    s = get_profile("System.Service.setState")
    if s:
        state = s["state"]
        if state == "on":
            start()
    else:
        start()

def status():
    ret = run("/usr/sbin/ejabberdctl --node ejabberd@localhost status")
    if ret != 0:
        return False
    return True
