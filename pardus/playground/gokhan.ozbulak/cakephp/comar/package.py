#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.chmod("/usr/share/php5/cakephp/app/tmp", 0777)
    for root, dirs, files in os.walk("/usr/share/php5/cakephp/app/tmp"):
        for name in dirs:
            os.chmod(os.path.join(root, name), 0777)
