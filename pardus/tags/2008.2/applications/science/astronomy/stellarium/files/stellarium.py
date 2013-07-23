#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Wrapper script or stellarium. It has initialization problems with tr_TR.UTF-8 locale.
# You can change the language of programme by clicking configuration window inside it

import subprocess
import sys
import os

os.environ["LC_ALL"] = "en_US.UTF-8"
os.environ["LANG"] = "en_US.UTF-8"

args = " ".join(sys.argv[1:])
subprocess.call(["/usr/bin/stellarium-bin", args])
