import os

def postInstall():
    os.system("/usr/lib/libgphoto2/print-camera-list udev-rules-0.98 mode 660 group pnp > /etc/udev/rules.d/60-libgphoto2.rules")
    os.system("/usr/lib/libgphoto2/print-camera-list hal-fdi > /usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2.fdi")
    os.system("/usr/lib/libgphoto2/print-camera-list hal-fdi-device > /usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2-device.fdi")

def preRemove():
    files = ["/etc/udev/rules.d/60-libgphoto2.rules", 
            "/usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2.fdi", 
            "/usr/share/hal/fdi/information/10freedesktop/10-camera-libgphoto2-device.fdi"]

    for f in files:
        if os.path.exists(f):
            os.unlink(f)
