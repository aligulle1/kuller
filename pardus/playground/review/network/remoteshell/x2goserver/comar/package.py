#!/usr/bin/python

import os
import fileinput
import sys

x2goSudoersLine=r"%users ALL=(ALL) NOPASSWD: /usr/bin/x2gopgwrapper"

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
                line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # add database directory and create the session database
    if not os.path.exists("/var/db/x2go/x2go_sessions"):
        os.mkdir("/var/db/x2go")
        os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
        os.system("/usr/lib/x2go/script/x2gosqlite.sh")

    # add the necessary sudoers line. This is necessary to make users be able to login through x2go
    f = open("/etc/sudoers", "a")
    f.write("# x2goserver needs this line to work correctly\n")
    f.write(x2goSudoersLine+"\n")
    f.close()
    
def postRemove():

    # remote the sudoers addition that we made
    replaceAll("/etc/sudoers", "# x2goserver needs this line to work correctly\n", "")
    replaceAll("/etc/sudoers", x2goSudoersLine+"\n", "")
