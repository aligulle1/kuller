#!/usr/bin/python
# -*- coding: utf-8 -*-

# A script to walk through svn subdirectories and update them

import os, subprocess

useColor = True
cmd = "svn up"
repoRoots = []
# Color characters
colors = {'red'       : '\x1b[31;01m',
         'blue'       : '\x1b[34;01m',
         'cyan'       : '\x1b[36;01m',
         'gray'       : '\x1b[30;01m',
         'green'      : '\x1b[32;01m',
         'light'      : '\x1b[37;01m',
         'yellow'     : '\x1b[33;01m',
         'magenta'    : '\x1b[35;01m',
         'reddark'    : '\x1b[31;0m',
         'bluedark'   : '\x1b[34;0m',
         'cyandark'   : '\x1b[36;0m',
         'graydark'   : '\x1b[30;0m',
         'greendark'  : '\x1b[32;0m',
         'magentadark': '\x1b[35;0m',
         'normal'     : '\x1b[0m'}


def colorize(msg, color):
    global useColor
    if not useColor:
        return msg
    else:
        return "%s%s%s" % (colors[color], msg, colors['normal'])

def updateRepos(repos):
    global cmd
    for repo in repos:
            command = cmd + " " + repo
            print "%s %s" %(colorize("Updating %s repository.", 'green') % (repo.split("/")[-1]), colorize("("+repo+")", 'cyan'))
            #TODO: control output, without updates 'At Revision' messages keeps shell busy
            p = subprocess.Popen(command, shell=True)

def getSvnRootDirs(startFrom=os.environ.get("HOME")):
    global repoRoots
    for root, dirs, files in os.walk(startFrom):
        if ".svn" in dirs:
            repoRoots.append(root)
            # delete the subdirs to stop recursion
            del dirs[:]
    return sorted(repoRoots)

if __name__ == "__main__":
    repos = getSvnRootDirs()
    updateRepos(repos)
