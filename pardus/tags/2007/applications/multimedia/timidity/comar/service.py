serviceType = "local"
serviceDesc = _({"en": "Timidity Virtual MIDI Sequencer for Alsa",
                 "tr": "Timidity Sanal MIDI Ardışımlayıcı"})

from comar.service import *
import os

def start():
    call("System.Service.start", "alsa-utils")

    if config.get("USE_ESOUND", "") == "yes":
        call("System.Service.start", "esound")

    # set up sound fonts
    patchset = config.get("PATCHSET", "shompatches")
    currentlink = "/usr/share/timidity/current"

    try:
        currentpatch = os.readlink(currentlink)
    except:
        currentpatch = None

    if patchset != currentpatch:
        if not os.path.exists("/usr/share/timidity/%s" % patchset) and not os.path.exists(patchset):
            fail("Failed to set patchset %s for Timidity" % patchset)
        else:
            if currentpatch:
                os.unlink(currentlink)
            os.symlink(patchset, currentlink)

    if config.get("TIMIDITY_PCM_NAME", "") != "":
        loadEnvironment()
        os.environ["TIMIDITY_PCM_NAME"]=config.get("TIMIDITY_PCM_NAME")

    ret = run("start-stop-daemon --start --quiet --background \
               --make-pidfile --pidfile /var/run/timidity.pid \
               --exec /usr/bin/timidity -- -iA %s" % config.get("TIMIDITY_OPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/timidity.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/timidity.pid")
