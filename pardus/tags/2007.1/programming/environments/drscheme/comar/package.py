#!/usr/bin/python

import os

def postInstall():
	os.system("/usr/share/drscheme/bin/setup-plt")
