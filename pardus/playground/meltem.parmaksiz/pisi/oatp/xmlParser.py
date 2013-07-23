#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import sys
import piksemel

import utils
dryrun = None
change = []

def getNodeTree(data):
    return piksemel.parseString(data)

def setPackageName(nod):
    global packagename

    name = nod.getTag("Source").getTagData("Name")
    version =  nod.getTag("Package").getTag("History").tags("Update").next().getTagData("Version")
    architecture =nod.getTag("Package").getTagData("Architecture")

    packagename = "%s32-%s-%s.pisi" % ( name, version, architecture.replace("_","-"))

def fixMetadataXML(nod_tree):
    #global change

    setPackageName(nod_tree)
    entries_path = nod_tree.getTag("Package").getTag("Files").tags("Path")

    for entry_path  in entries_path:
        path_data = entry_path.firstChild().data()
        fixed_path= utils.correctPath( path_data )

        #if  path_data != fixed_path:
        #    change.append( path_data)

        if fixed_path == None:
            entry_path.hide()
        else:
            entry_path = entry_path.setData( fixed_path )

    nod_tree.getTag("Package").getTag("Architecture").setData("x86_64")

    setPackageName(nod_tree)
    return nod_tree


def fixFilesXML(nod_tree):
    global change

    entries_files = nod_tree.tags( "File" )

    for entry_file in entries_files:

        path_data = entry_file.getTagData( "Path" )
        fixed_path = utils.correctPath( path_data )

        if fixed_path == None:
            entry_file.hide()
        else:
            change.append( path_data )
            entry_file.getTag( "Path" ).setData( fixed_path )


    return nod_tree



