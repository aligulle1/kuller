# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Automatic Bug Reporting Tool",
                 "tr": "Otomatik Hata Raporlama Aracı"
                 })

PID_FILE="/var/run/abrtd.pid"

PATTERN_FILE="/proc/sys/kernel/core_pattern"
SAVED_PATTERN_FILE="/var/run/abrt/saved_core_pattern"
HOOK_BIN="/usr/libexec/abrt-hook-ccpp"
PATTERN="|%s /var/spool/abrt %%s %%c %%p %%u %%g %%t %%h %%e" % HOOK_BIN

# core_pipe_limit specifies how many dump_helpers can run at the same time
# 0 - means unlimited, but it's not guaranteed that /proc/<pid> of crashing
#     process will be available for dump_helper.
# 4 - means that 4 dump_helpers can run at the same time (the rest will also
#     run, but they will fail to read /proc/<pid>).
#
# This should be enough for ABRT, we can miss some crashes, but what are
# the odds that more processes crash at the same time? And moreover,
# do people want to save EVERY ONE of the crashes when they have
# a crash storm? I don't think so.
# The value of 4 has been recommended by nhorman.
#
CORE_PIPE_LIMIT_FILE="/proc/sys/kernel/core_pipe_limit"
CORE_PIPE_LIMIT="4"

def install_coredump_hook():
    current_pattern  = open(PATTERN_FILE, 'r').read().strip()

    if current_pattern != PATTERN:
        # pattern is not already modified
        open(SAVED_PATTERN_FILE, 'w').write("%s\n" % current_pattern)
        open(PATTERN_FILE, 'w').write(PATTERN)

    current_pipe_limit = open(CORE_PIPE_LIMIT_FILE, 'r').read().strip()

    if current_pipe_limit == "0":
        open(CORE_PIPE_LIMIT_FILE, 'w').write(CORE_PIPE_LIMIT)

def restore_core_pattern():
    import os
    if os.path.isfile(SAVED_PATTERN_FILE):
        saved_pattern = open(SAVED_PATTERN_FILE, 'r').read().strip()
        open(PATTERN_FILE, 'w').write(saved_pattern)
        os.unlink(SAVED_PATTERN_FILE)

@synchronized
def start():
    install_coredump_hook()
    startService(command="/usr/sbin/abrtd",
                 pidfile=PID_FILE,
                 donotify=True)

    # This script is meant to be run once at system startup after abrtd is up
    # and running. It moves all vmcore directories in /var/crash
    # (which are presumably created by kdump) to abrtd spool directory.
    run("/usr/sbin/abrt-harvest-vmcore")

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)
    restore_core_pattern()

def status():
    return isServiceRunning(PID_FILE)
