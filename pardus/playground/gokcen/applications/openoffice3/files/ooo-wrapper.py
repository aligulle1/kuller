#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import *

ooo_program_path = "/opt/OpenOffice.org/bin/"
program = os.path.join(ooo_program_path, os.path.basename(sys.argv[0]))
process = None

files = sys.argv[1:]
if files:
    for file in files:
        process = Popen(['kio-to-local', program, file])
else:
    process = Popen([program])

os.waitpid(process.pid,0)
