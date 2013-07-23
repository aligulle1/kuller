#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def installGconfSchemas(filepath):
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    parse = piksemel.parse(filepath)
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/gconf/schemas"):
            os.system("/usr/bin/gconftool-2 --makefile-install-rule /%s" % path)

def uninstallGconfSchemas(filepath):
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    parse = piksemel.parse(filepath)
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/gconf/schemas"):
            os.system("/usr/bin/gconftool-2 --makefile-uninstall-rule /%s" % path)

def setupPackage(metapath, filepath):
    installGconfSchemas(filepath)

def cleanupPackage(metapath, filepath):
    uninstallGconfSchemas(filepath)
