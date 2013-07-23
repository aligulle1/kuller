#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import sys
import os
import urllib
import pisi

STATEFILE = "/var/pisi/pisiUpgradeState"

def set_step(step):
   open(STATEFILE, "w").write(step)

def started(operation=""):
   notify("System.Upgrader", "started", operation)

def finished(operation=""):
   notify("System.Upgrader", "finished", operation)

def cancelled(operation=""):
   notify("System.Upgrader", "cancelled", operation)

class UpgraderUI(pisi.ui.UI):

   def __init__(self, total):
      pisi.ui.UI.__init__(self, total)
      self.installed = 0
      self.total = total

   def error(self, msg):
      pass

   def warning(self, msg):
      pass

   def notify(self, event, **keywords):
      if event == pisi.ui.installing:
         pkgname = keywords["package"].name
         self.installed += 1
         notify("System.Upgrader", "status", ("installing", pkgname, self.total, self.installed))

   def ack(self, msg):
      return True

   def confirm(self, msg):
      return True

   def display_progress(self, operation, percent, info="", **kw):
      pass

def step(func):
    """
    Decorator for synchronizing privileged functions
    """
    def wrapper(*__args,**__kw):
        operation = "System.Upgrader.%s" % func.func_name

        set_step(func.func_name)
        started(operation)
        try:
            func(*__args,**__kw)
        except KeyboardInterrupt:
            cancelled()
            return
        finished(operation)

    return wrapper

def reboot():
   notify("System.Upgrader", "needsreboot")
   sys.exit(0)
   # dbus-send --system --dest=org.freedesktop.Hal --type=method_call --print-reply /org/freedesktop/Hal/devices/computer  org.freedesktop.Hal.Device.SystemPowerManagement.Reboot

def get_extras():
   packages = []
   for line in urllib.urlopen("http://svn.pardus.org.tr/uludag/trunk/pardus-upgrade/2008_2009.list").readlines():
      ls = line.strip()
      if ls.startswith("#") or not ls:
         continue
      else:
         packages.append(ls)

   return pisi.api.get_install_order(packages)

def get_upgrades():
   replaces = pisi.api.list_replaces()
   packages = set(pisi.api.list_upgradable())

   # replaced package should be downloaded
   for pkg in replaces:
      if pkg in packages:
         packages.remove(pkg)
         packages.add(replaces[pkg])

   return pisi.api.get_upgrade_order(packages)

@step
def prepare():
    pass

@step
def setRepositories():
   for name in pisi.api.list_repos():
      pisi.api.remove_repo(name)

   pisi.api.add_repo("pardus-2009", "http://packages.pardus.org.tr/pardus-2009/pisi-index.xml.bz2")
   pisi.api.add_repo("contrib-2009", "http://packages.pardus.org.tr/contrib-2009/pisi-index.xml.bz2")
   pisi.api.update_repos(pisi.api.list_repos())

@step
def download():
   packages = set(get_upgrades() + get_extras())
   for index, package in enumerate(packages):
      notify("System.Upgrader", "status", ("downloading", len(packages), index + 1))
      pisi.api.fetch([package], "/var/cache/pisi/packages")

@step
def upgrade():

   def install_packages():
      pisi.api.upgrade([])

   def fix_policykit_auths():
      if os.path.exists('/var/lib/PolicyKit'):
         os.system('sed -i -e "s/python2.5/python2.6/" /var/lib/PolicyKit/*.auths')

   def install_extra_packages():
      pisi.api.install(get_extras(), ignore_file_conflicts=True)

   def configure_packages():
      notify("System.Upgrader", "status", ("configuring", ))
      # configurePending must be run with new COMAR
      os.system("python -c 'import pisi;pisi.api.set_comar_updated(True);pisi.api.configure_pending()'")

   def fix_kdm():
      # From a developer who did not want to give his name :)
      if os.path.exists("/etc/X11/kdm/kdmrc.newconfig"):
         if os.popen("/usr/kde/4/bin/kreadconfig --file /etc/X11/kdm/kdmrc --group \"X-:0-Core\" --key AutoLoginEnable").read().strip().lower() == "true":
            user = os.popen("/usr/kde/4/bin/kreadconfig --file /etc/X11/kdm/kdmrc --group \"X-:0-Core\" --key AutoLoginUser").read().strip()
            os.system("/usr/kde/4/bin/kwriteconfig --file /etc/X11/kdm/kdmrc.newconfig --group \"X-:0-Core\" --key AutoLoginEnable true")
            os.system("/usr/kde/4/bin/kwriteconfig --file /etc/X11/kdm/kdmrc.newconfig --group \"X-:0-Core\" --key AutoLoginUser %s" % user)
            os.system("/usr/kde/4/bin/kwriteconfig --file /etc/X11/kdm/kdmrc.newconfig --group \"X-:0-Core\" --key AutoLoginLocked false")

         os.system("/bin/mv -f /etc/X11/kdm/kdmrc.newconfig /etc/X11/kdm/kdmrc")

   def fix_kaptan():
      os.system("rm -rf /home/*/.kde/share/config/kaptanrc")

   # Fatih's brilliant reboot hack :)
   # KDE3 does not reboot in any way, just quits and sits tight in console login screen when you use
   # ksmserver's dcop logout call. Because kde3 packages are removed while upgrading, the binaries and
   # scripts that are used to finish rebooting process does not exist. So a forced reboot is needed.
   def fatihs_reboot_hack():
      open("/usr/kde/3.5/share/config/kdm/Xreset", "w").write("#!/bin/bash\n/sbin/reboot\n")

   packages = set(get_upgrades() + get_extras())
   ui = UpgraderUI(len(packages))
   pisi.api.set_userinterface(ui)
   pisi.api.set_comar(False)
   
   install_packages()
   fix_policykit_auths()
   install_extra_packages()
   configure_packages()
   fix_kdm()
   fix_kaptan()
   fatihs_reboot_hack()

@step
def cleanup(self):
   pass
