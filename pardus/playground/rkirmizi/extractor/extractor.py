#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import popen,path,chdir,walk,listdir,remove
from string import split
from sys import argv

directory = argv[-1]
list = []
delete_files = []

for root,dirs,files in walk(directory):
    for dir in dirs:
        list.append(path.join(root, dir))
    for file in files:
        delete_files.append(path.join(root, file))


def unrar(path):
    for lines in popen('unrar e %s' % path):
        print lines

def unzip(path):
    for lines in popen('unzip %s' % path):
        print lines

for dirs in list:
    for file in listdir(dirs):
        if file.endswith('rar'):
            chdir(dirs)
            unrar(path.join(dirs, file))
        if file.endswith('zip'):
            chdir(dirs)
            unzip(path.join(dirs, file))

###################################
# print '\nCleaning old files...' #
# for files in delete_files:      #
#     remove(files)               #
#                                 #
###################################
