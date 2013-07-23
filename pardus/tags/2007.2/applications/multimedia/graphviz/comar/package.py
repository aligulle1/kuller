#!/usr/bin/python

import os

def postInstall():
    # write layout's config
    os.system("/usr/bin/dot -c")
