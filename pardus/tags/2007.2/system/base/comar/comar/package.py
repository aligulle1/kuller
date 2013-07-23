import os
import time
import socket

def postInstall():
    comar_pid = "/var/run/comar.pid"
    
    data = file("/var/db/comar/format").read()
    if data.split("\n")[0] == "1":
        # Possibly updating from release 28
        file("/var/db/comar/format", "w").write("2")
        # We cant stop running Comar in that case, so just start the new one
        try:
            os.unlink(comar_pid)
            os.unlink("/var/run/comar.socket")
        except OSError:
            pass
        os.system("/sbin/start-stop-daemon -b --start --pidfile %s --make-pidfile --exec /usr/bin/comar" % comar_pid)
        return
    
    # Tell running comar to go background and start shutdown process
    os.system("/sbin/start-stop-daemon --stop --pidfile %s" % comar_pid)
    # Wait until it closes its socket
    timeout = 10
    while timeout > 0:
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect("/var/run/comar.socket")
        except socket.error:
            break
        time.sleep(0.1)
        timeout -= 0.1
    # New comar will start taking orders from socket
    try:
        os.unlink(comar_pid)
    except OSError:
        pass
    
    os.system("/sbin/start-stop-daemon -b --start --pidfile %s --make-pidfile --exec /usr/bin/comar" % comar_pid)
