#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.popen('lsmod | grep binfmt_misc').read().strip() == "":
        os.system("modprobe binfmt_misc")

    os.system('sysctl abi.vsyscall32=0')
    os.system('sysctl vm.mmap_min_addr=0')
