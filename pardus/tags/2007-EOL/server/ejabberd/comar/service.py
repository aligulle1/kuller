from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Ejabberd Jabber Server",
                 "tr": "Ejabberd Jabber Sunucusu"})

def start():
    loadEnvironment()

    # Use more than 1024 connections... (~6MB more memory will be used)
    os.environ["ERL_MAX_PORTS"] = "32000"

    ret = run('''/usr/bin/erl \
               -pa /usr/lib/erlang/lib/ejabberd-1.1.3/ebin \
               -sname ejabberd \
               -s ejabberd \
               -ejabberd config \"/etc/jabber/ejabberd.cfg\" \
                         log_path \"/var/log/jabber/ejabberd.log\" \
               -mnesia dir \"/var/lib/jabber/spool\" \
               -kernel inetrc \"/etc/jabber/inetrc\" \
               -detached''')
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/ejabberdctl ejabberd@localhost stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def ready():
    s = get_profile("System.Service.setState")
    if s:
        state = s["state"]
        if state == "on":
            start()
    else:
        start()

def status():
    ret = run("/usr/sbin/ejabberdctl ejabberd@localhost status")
    if ret != 0:
        return False
    return True
