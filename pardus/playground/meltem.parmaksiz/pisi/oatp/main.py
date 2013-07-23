#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import sys
import shutil

import zipArchive
import tarArchive
import lzmaArchive
import xmlParser
import utils


def main( package ):
    global change_list
    global packagename

    zipArchive.extractAll( package)

    data = file( "files.xml" ).read()
    node_tree = xmlParser.getNodeTree(data)
    node_tree =xmlParser.fixFilesXML(node_tree)

    if xmlParser.change:
        xmlParser.change.append( package )
        change_list.append( xmlParser.change )
        xmlParser.change = None

    else:
         print "not changing %s "  % package

    if not dryrun:
        data = utils.convertXMLtoString(node_tree)
        utils.reproduceFile("files.xml", data )

        data = file("metadata.xml").read()
        node_tree = xmlParser.getNodeTree(data)
        node_tree = xmlParser.fixMetadataXML(node_tree)
        data = utils.convertXMLtoString(node_tree)
        utils.reproduceFile("metadata.xml", data )

        print "unpacklzma"
        lzmaArchive.unpackLZMA( "install.tar.xz", "old.tar" )

        print "copy tar archive"
        tarArchive.copyTarArc( "old.tar",  "install.tar",  "install")

        os.unlink("old.tar")
        os.unlink("install.tar.xz")
        shutil.rmtree("install")

        #FIXME: use pyliblzma
        os.system("xz -9 install.tar")

        zipArchive.createZipArchive( temp_directory, xmlParser.packagename)


def inform():
    for change in change_list:
        print change


if __name__ == "__main__":

    dryrun = 0
    change_list  = []

    if "dryrun" in sys.argv :
        dryrun = 1
        sys.argv.remove("dryrun")

    if len(sys.argv) < 2:
        print "Usage: %s  <pisi_packages_directory>" % sys.argv[0]
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print "%s does not exists" % sys.argv[1]
        sys.exit(1)

    pisi_directory = sys.argv[1]
    pisi_list = glob.glob1( pisi_directory, "*6.pisi" )

    temp_directory =  "/tmp/oatp"

    olddir = os.getcwd()

    for pisi in pisi_list:
        utils.makeDir(temp_directory)
        os.chdir(temp_directory)
        main( os.path.join(pisi_directory,pisi) )

    if dryrun:
        inform( )

    os.chdir(olddir)
