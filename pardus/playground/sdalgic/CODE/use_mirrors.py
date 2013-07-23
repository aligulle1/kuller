#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# AUTHOR : Serdar Dalgic
# EMAIL  : serdar@pardus.org.tr
#

'''
A small script to change direct addresses to use mirrors for perl modules.
'''

import os
import sys

TARGET_PATH="/home/sdalgic/PARDUS_SVN/PARDUS/2009/devel/programming/language/perl"

if __name__ == "__main__":
    list = sys.argv[1]

    os.chdir(TARGET_PATH)

    if os.path.exists(list):
        for package in open(list, "r").readlines():
            ret = []
            for l in open(package.split("\n")[0], "r").readlines():
                if "<Archive" in l:
                    if "CPAN" in l:
                        nls = l.split("http")[0]
                        nl = nls + "mirrors://cpan/" + l.split("CPAN/")[1]
                        ret.append(nl)
                    else:
                        ret.append(l)
                else:
                    ret.append(l)

            open(package.split("\n")[0], "w").write("".join(ret))

