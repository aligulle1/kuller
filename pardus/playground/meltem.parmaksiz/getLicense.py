#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import piksemel
import zipfile
from sets import Set

metadata_file = "metadata.xml"
listoflisence = []


def getLicense(pisi):
    zip_archive = zipfile.ZipFile(pisi, "r")
    data = zip_archive.read(metadata_file)

    nod_tree = piksemel.parseString(data)
    license = nod_tree.getTag('Package').getTagData('License')

    listoflisence.append(license)
    print "%s package lisence  : %s " % ( pisi , license)

    zip_archive.close()


def  uniqueList(seq):
    set = Set(seq)
    return list(set)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "You must give a directory name for pisi files"
    elif not os.path.exists(sys.argv[1]):
        print "%s does not exists" % sys.argv[1]
    else:
        olddir = os.getcwd()

        directory = sys.argv[1]
        os.chdir(directory)

        for i in os.listdir(directory):
            if i.endswith(".pisi"):
                getLicense(i)


        print "---UniqueListOfLicense---"
        print "%d packages are viewed " %  len(listoflisence)

        for i in  uniqueList(listoflisence):
            print i

        os.chdir(olddir)
