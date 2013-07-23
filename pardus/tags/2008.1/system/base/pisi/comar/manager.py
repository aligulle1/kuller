#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2007 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import locale
import string

# FIXME: later this will be Comar's job
systemlocale = open("/etc/mudur/locale", "r").readline().strip()

# for pisi
os.environ["LC_ALL"] = systemlocale

# for system error messages
locale.setlocale(locale.LC_ALL, systemlocale)

notify("System.Manager", "status", ("started"))

try:
    import pisi.api
    import pisi.db
    import pisi.ui
    import pisi.util as util
    import pisi.configfile
    from pisi.version import Version
except KeyboardInterrupt:
    notify("System.Manager", "cancelled", None)

class UI(pisi.ui.UI):
    def error(self, msg):
        notify("System.Manager", "error", ("%s" % msg))

    def warning(self, msg):
        notify("System.Manager", "warning", ("%s" % msg))

    def notify(self, event, **keywords):
        if event == pisi.ui.installing:
            pkgname = keywords["package"].name
            notify("System.Manager", "status", ("installing", pkgname))
        elif event == pisi.ui.configuring:
            pkgname = keywords["package"].name
            notify("System.Manager", "status", ("configuring", pkgname))
        elif event == pisi.ui.extracting:
            pkgname = keywords["package"].name
            notify("System.Manager", "status", ("extracting", pkgname))
        elif event == pisi.ui.updatingrepo:
            reponame = keywords["name"]
            notify("System.Manager", "status", ("updatingrepo", reponame))
        elif event == pisi.ui.removing:
            pkgname = keywords["package"].name
            notify("System.Manager", "status", ("removing", pkgname))
        elif event == pisi.ui.cached:
            total = str(keywords["total"])
            cached = str(keywords["cached"])
            notify("System.Manager", "status", ("cached", total, cached))
        elif event == pisi.ui.installed:
            notify("System.Manager", "status", ("installed"))
        elif event == pisi.ui.removed:
            notify("System.Manager", "status", ("removed"))
        elif event == pisi.ui.upgraded:
            notify("System.Manager", "status", ("upgraded"))
        elif event == pisi.ui.packagestogo:
            notify("System.Manager", "status", ("order"))
        else:
            return

    def ack(self, msg):
        return True

    def confirm(self, msg):
        return True

    def display_progress(self, operation, percent, info="", **kw):
        if operation == "fetching":
            out = (operation, kw["filename"],int(percent),int(kw["rate"]),kw["symbol"], kw["downloaded_size"],kw["total_size"])
        else:
            out = (operation, int(percent), info)
        notify("System.Manager", "progress", out)

def _init_pisi():
    ui = UI()
    try:
        pisi.api.set_userinterface(ui)
    except KeyboardInterrupt:
        cancelled()

def cancelled():
    notify("System.Manager", "cancelled", None)

def finished(operation=""):
    if operation in ["System.Manager.setCache", "System.Manager.installPackage", "System.Manager.removePackage", "System.Manager.updatePackage"]:
        __checkCacheLimits()

    notify("System.Manager", "finished", (operation))

def installPackage(package=None):
    _init_pisi()
    if package:
        try:
            package = package.split(",")
            pisi.api.install(package, ignore_file_conflicts=True)
        except KeyboardInterrupt:
            cancelled()
        except Exception,e:
            fail(unicode(e))
    finished("System.Manager.installPackage")

def updatePackage(package=None):
    _init_pisi()
    try:
        if package is None:
            package = []
        else:
            package = package.split(",")
        pisi.api.upgrade(package)
    except KeyboardInterrupt:
        cancelled()
    except Exception,e:
        fail(unicode(e))
    finished("System.Manager.updatePackage")

def removePackage(package=None):
    _init_pisi()
    if package:
        try:
            package = package.split(",")
            pisi.api.remove(package)
        except KeyboardInterrupt:
            cancelled()
        except Exception, e:
            fail(unicode(e))
    finished("System.Manager.removePackage")

def updateRepository(repository=None):
    _init_pisi()
    if repository:
        try:
            notify("System.Manager", "status", ("updatingRepo", str(repository)))
            pisi.api.update_repo(repository)
        except KeyboardInterrupt:
            cancelled()
        except Exception, e:
            fail(unicode(e))
    finished("System.Manager.updateRepository")

def updateAllRepositories():
    _init_pisi()
    try:
        for repo in pisi.db.repodb.RepoDB().list_repos():
            notify("System.Manager", "status", ("updatingRepo", str(repo)))
            pisi.api.update_repo(repo)
    except KeyboardInterrupt:
        cancelled()
    except Exception, e:
        fail(unicode(e))
    finished("System.Manager.updateAllRepositories")

def addRepository(name=None,uri=None):
    _init_pisi()
    if name and uri:
        try:
            pisi.api.add_repo(name,uri)
        except KeyboardInterrupt:
            cancelled()
        except Exception, e:
            fail(unicode(e))
    finished("System.Manager.addRepository")

def removeRepository(repo=None):
    _init_pisi()
    if repo:
        try:
            pisi.api.remove_repo(repo)
        except KeyboardInterrupt:
            cancelled()
        except Exception, e:
            fail(unicode(e))
    finished("System.Manager.removeRepository")

def setRepositories(repos=None):
    _init_pisi()
    if repos:
        try:
            notify("System.Manager", "status", ("savingrepos"))
            oldRepos = pisi.db.repodb.RepoDB().list_repos()

            for repo in oldRepos:
                pisi.api.remove_repo(repo)

            for repo in repos:
                pisi.api.add_repo(repo[0], repo[1])

        except KeyboardInterrupt:
            cancelled()
        except Exception, e:
            fail(unicode(e))
    finished("System.Manager.setRepositories")

# ex: setConfig("general", "bandwidth_limit", "30")
def setConfig(category, name, value):
    config = pisi.configfile.ConfigurationFile("/etc/pisi/pisi.conf")
    config.set(category, name, value)

    config.write_config()
    finished("System.Manager.setConfig")

def setCache(enabled, limit):
    config = pisi.configfile.ConfigurationFile("/etc/pisi/pisi.conf")
    config.set("general", "package_cache", str(enabled))
    config.set("general", "package_cache_limit", str(limit))

    config.write_config()
    finished("System.Manager.setCache")

def clearCache(cacheDir, limit):
    _init_pisi()
    try:
        pisi.api.clearCache(int(limit) == 0)
    except KeyboardInterrupt:
        cancelled()
    except Exception, e:
        fail(unicode(e))
    finished("System.Manager.clearCache")

def takeSnapshot():
    _init_pisi()
    try:
        notify("System.Manager", "status", "takingSnapshot")
        pisi.api.snapshot()
    except Exception, e:
        fail(unicode(e))
    finished("System.Manager.takeSnapshot")

def takeBack(operation):
    _init_pisi()
    try:
        notify("System.Manager", "status", "takingBack")
        pisi.api.takeback(operation)
    except Exception, e:
        fail(unicode(e))
    finished("System.Manager.takeBack")

def __checkCacheLimits():
    cached_pkgs_dir = "/var/cache/pisi/packages"
    config = pisi.configfile.ConfigurationFile("/etc/pisi/pisi.conf")
    cache = config.get("general", "package_cache")
    if cache == "True":
        limit = config.get("general", "package_cache_limit")

        # If PackageCache is used and limit is 0. It means limitless.
        if limit and int(limit) != 0:
            clearCache(cached_pkgs_dir, int(limit) * 1024 * 1024)
    elif cache == "False":
        clearCache(cached_pkgs_dir, 0)
