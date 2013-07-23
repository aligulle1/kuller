#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, sys
import locale

if len(sys.argv) != 2:
    print "usage: mkdodoc.py /path/to/buildfiles\nexample: /home/user/mkdodoc.py /var/pisi/bash-3.2-18/work/bash-3.2/"
    exit()

if os.path.isdir(sys.argv[1]) == False:
    print "Please heck path, can't find path"
    exit()

files = os.listdir(sys.argv[1])

files.sort()

dodoc = []

for file in files:
    if file[0].isupper():
        if file.startswith("Makefile"):
            pass
        elif file.startswith("SCons"):
            pass
        else:
            dodoc.append(file)

result = "    # pisitools.dodoc(\""

for entry in dodoc:
    result = result + entry
    result = result + "\", \""

dodocline = result[:-3] + ")"

yesexpr = re.compile(locale.nl_langinfo(locale.YESEXPR))
prompt = "add to actions.py as comment? (yes/no): "
s = raw_input(prompt.encode('utf-8'))

if yesexpr.search(s) != None:
    actions = open("actions.py", "a")
    actions.writelines("\n" + dodocline + "\n")
    print dodocline
    print "\nentry added to actions.py succesfully"
    exit()

elif yesexpr.search(s) == None:
    print "\n\n"
    print dodocline
    exit()
