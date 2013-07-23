#!/usr/bin/python
# -*- coding: utf-8 -*-

# A script to check and change Build Dependencies of a package
#   to dependency-devel packages.

#usage example change_deps_to_dep-devel vlc 2011/devel/pisi-index.xml

import os 
import sys
import piksemel
import bz2
import pisi

index_file="/home/sdalgic/2011/devel/pisi-index.xml"

wildcards = ["devel"]

def getXmlData(_file):
    if os.path.exists(_file):
        if _file.endswith(".bz2"):
            indexdata = bz2.decompress(file(_file).read())
            return piksemel.parseString(indexdata)
        else:
            return piksemel.parse(_file)
    else:
        print "%s not found" % _file
        sys.exit(1)


if __name__ == "__main__":
    "ortada kuyu var yandan gec ;)"

#    if len(sys.argv) != 3:
#        print " usage:"
#        print "%s <package> <repo index file>" % sys.argv[0]
#        sys.exit(1)

    Build_dep_list = []
    for build_dep in pisi.specfile.SpecFile("%s/pspec.xml" % sys.argv[1]).source.buildDependencies:
        Build_dep_list.append(build_dep.name())

    for wildcard in wildcards:
        Build_dep_list = filter(lambda x: not(wildcard in x), Build_dep_list)

    if "pulseaudio" in Build_dep_list:
        pulseaudio_exists = True

    ix = getXmlData(index_file)

    pkglist = []

    for node in ix.tags("SpecFile"):
        for pkgnode in node.tags("Package"):
            if "devel" in pkgnode.getTagData("Name"):
                pkglist.append(pkgnode.getTagData("Name"))

        #pkglist.append(pkgnode.getTagData("Name") for pkgnode in node.tags("Package") if "devel" in pkgnode.getTagData("Name"))

    print "These BuildTime deps should be changed:"
    for dep in Build_dep_list:
        if "%s-devel" % dep in pkglist:
            print "\t" + dep + " -> " + dep + "-devel"









