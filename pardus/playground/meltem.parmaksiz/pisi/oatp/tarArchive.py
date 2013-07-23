#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import utils
import tarfile

def extractAllTarArc(tar_arc, dest=""):
    if  dest:
        utils.makeDir(dest)
    tf = tarfile.open(tar_arc, 'r')
    tf.extractall(dest)
    tf.close()

def extractMemberTarArc(member, tar_arc, dest=""):
    tf = tarfile.open(tar_arc, mode='r')
    tf.extract(member, dest)
    tf.close()

def readMemberZipArc(member, tar_arc):
    tf = tarfile.open(tar_arc, mode='r')
    data = tar.extractfile(member).read()
    tf.close()
    return data


def createTarArc(source_direct, tar_name):
    tf = tarfile.open(tar_name, mode='w')

    file_list = os.listdir(source_direct)
    file_list.sort()

    for fl in file_list:
        tf.add( os.path.join(source_direct, fl) , arcname=fl)

    tf.close()

def createTarArchive( file_list, tar_name ):
    tf = tarfile.open(tar_name, mode='w')

    for fl in file_list:
        tf.add( fl )

    tf.close()

def copyTarArc( old_tar, new_tar, temp_directory):
    old_tar = tarfile.open(old_tar, mode='r')

    members =  old_tar.getmembers()
    members.sort()

    utils.makeDir(temp_directory)
    for member in members:
        fixed_path =  utils.correctPath(member.name)

        if fixed_path :
            member.name = fixed_path
            old_tar.extract(member, path=temp_directory)

        createTarArc(temp_directory, new_tar)

    old_tar.close()


def main():
    if len(sys.argv) < 2:
        print "usage : "
        exit(1)

    if os.path.exists(sys.argv[1]):
        print "%s does not exists" % sys.argv[1]
        exit(1)

    if len(sys.argv) == 3:
        print "extract processing :   "
        extractAllTarArc(sys.argv[1], sys.argv[2])

    elif len(sys.argv) == 2:
        print "compress processing :  "
        createTarArc(sys.argv[1], "%s.tar" % sys.argv[1])


if __name__ == "__main__":

   copyTarArc("old.tar", "new.tar", "/tmp/oatp")
