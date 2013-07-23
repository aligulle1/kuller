#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # recursively chwon /var/spool/svxlink as VoiceMail plugin
    # needs to write data to it.

    os.system("chown -R svxlink:daemon /var/spool/svxlink")

