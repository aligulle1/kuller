#!/usr/bin/python
# -*- coding: utf-8 -*- 
# create mo files and move them to their destination, for Pardus kde4
#using python messages_dir
import os,sys

paths = sys.argv[1:]

pofilenames=[]

for path in paths:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".po"):
                pofilenames.append(os.path.join(root, file.split(".")[0]))

for po in pofilenames:
    print "%s.po is being converted as %s.mo" % (po, po)
    os.popen("msgfmt -v %s.po -o %s.mo" % (po, po))
    print "%s.mo moved to its destination" % po
#move my firends to ...
    os.system("mv %s.mo /usr/kde/4/share/locale/tr/LC_MESSAGES/" % po)
#clean obsolete desktop.mo files
os.system("rm -rf /usr/kde/4/share/locale/tr/LC_MESSAGES/desktop_*")
print "*desktop.mo files deleted\nDone..."



