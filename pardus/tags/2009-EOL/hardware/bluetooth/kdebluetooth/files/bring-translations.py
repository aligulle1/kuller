#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

topdircmake = """\
find_package(Gettext REQUIRED)
if (NOT GETTEXT_MSGMERGE_EXECUTABLE)
MESSAGE(FATAL_ERROR "Please install msgmerge binary")
endif (NOT GETTEXT_MSGMERGE_EXECUTABLE)
if (NOT GETTEXT_MSGFMT_EXECUTABLE)
MESSAGE(FATAL_ERROR "Please install msgmerge binary")
endif (NOT GETTEXT_MSGFMT_EXECUTABLE)
"""

cmd = "svn co https://svn.kde.org/home/kde/trunk/l10n-kde4/%s/messages/playground-network %s"

langs = ["pl", "tr", "nl", "de", "es", "it", "fr", "pt_BR", "ca", "sv"]

"""
os.makedirs("po-svn")
os.makedirs("po")

for l in langs:
    os.system(cmd % (l, l))
"""
os.chdir("po")
langs = []

for line in os.popen("find -name 'kbluetooth*po'").readlines():
    langs.append(os.path.dirname(line).split("./")[1])

langs = list(set(langs))

for d in [_d for _d in os.listdir(".") if _d not in langs]:
    os.system("rm -rf %s" % d)

f = open("CMakeLists.txt", "w")
f.write(topdircmake)

for l in langs:
    # Cleanup other po files
    map(os.unlink, set(glob.glob("%s/*.po" % l)).difference(glob.glob("%s/kbluetooth*.po" % l)))

    f.write("add_subdirectory(%s)\n" % l)
    open("%s/CMakeLists.txt" % l, "w").write("""\
file(GLOB _po_files *.po)
GETTEXT_PROCESS_PO_FILES(%s ALL INSTALL_DESTINATION ${LOCALE_INSTALL_DIR} ${_po_files} )
""" % l)

f.close()

os.chdir("..")

open("translations.patch", "w").write(os.popen("diff --exclude=.svn -Naur po-svn po").read().strip()+'\n')

os.system("svn revert CMakeLists.txt")
f = open("CMakeLists.txt", "a+").write("add_subdirectory(po)\n")
os.system("svn diff CMakeLists.txt >> translations.patch")
