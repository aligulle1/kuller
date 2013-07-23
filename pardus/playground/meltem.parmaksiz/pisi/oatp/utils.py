#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import shutil


def makeDir(path):
    cleanDir(path)
    os.makedirs(path)

def cleanDir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def getDirectoryFileName(filename):
    (path,name) = os.path.split(filename)
    return (path, name)

def convertXMLtoString(nod_tree):
    return nod_tree.toPrettyString()

def reproduceFile( file_name, data ):
    f = open( file_name, "w")
    f.write( data )
    f.close()

def correctPath( data) :
    for pattern in [r'usr/lib/',
                    r'lib/',
                    ]:
        regex = re.compile(pattern)

        if regex.search(data) :
            path = "%s32/" % pattern[:-1]
            return regex.sub(path, data)

    for pattern in [r'usr/bin/',
                    r'bin/',
                ]:
        regex = re.compile(pattern)

        if regex.search(data) :
            path = "%s32/" % pattern
            return regex.sub(path, data)

    return None


if __name__ == "__main__":
    print "util"
    print  correctPath("/home/lib/deen")
    print correctPath("bin/denem")
    print correctPath("/home/meltem/denemm")



