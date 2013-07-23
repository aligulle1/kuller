#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import zipfile

import utils

def extractAll(zip_archive, dest=""):
    if dest:
        utils.makeDir(dest)
    zf = zipfile.ZipFile(zip_archive)
    zf.extractall(path=dest )
    zf.close()

def extractMemberZipArc(member, zip_arc, dest=""):
    zf = zipfile.ZipFile(zip_arc)
    zf.extract(member, dest)
    zf.close()

def readMemberZipArc(member, zip_arc):
    zf = zipfile.ZipFile(zip_arc)
    data = zf.read(member)
    zf.close()
    return data

def addFiletoZipArc( zip_archive, file_name, arcname):
    zf = zipfile.ZipFile(zip_archive)
    zf.write(file_name, arcname)
    zf.close()

def createZipArchive(source, zip_name):
    zf = zipfile.ZipFile(zip_name, "w" )     # compression=ZIP_STORED (no compression)

    for root, dirs, files in os.walk(source):
        for name in files:
            fl = os.path.join(root, name)
            print fl.split("/",1)[1], "arc name ", fl, "added file "
            zf.write(fl, arcname=fl.split("/",1)[1])   #remove directory name
    zf.close()



def main():
    if len(sys.argv) < 2:
        print "usage : "
        exit(1)

    if os.path.exists(sys.argv[1]):
        print "%s does not exists" % sys.argv[1]
        exit(1)

    if len(sys.argv) == 3:
        print "extract processing :   "
        extractAll(sys.argv[1], sys.argv[2])

    elif len(sys.argv) == 2:
        print "compress processing :  "
        createZipArchive(sys.argv[1], "%s.pisi" % sys.argv[1])


if __name__ == "__main__":
    main()

