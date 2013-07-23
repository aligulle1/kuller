import os
import time
import socket

def postInstall():
    comar_pid = "/var/run/comar.pid"
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
    if os.path.exists(comar_pid):
        os.unlink(comar_pid)
    os.system("/sbin/start-stop-daemon -b --start --pidfile %s --make-pidfile --exec /usr/bin/comar" % comar_pid)
