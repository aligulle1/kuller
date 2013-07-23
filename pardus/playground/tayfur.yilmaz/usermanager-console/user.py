#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# User configuration tool for UserManager
#

#This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. Please read the COPYING file.
#

"""Interactive user configuration tool for UserManager"""

import sys
import uuid
from optparse import OptionParser

from usermanager import UserManager,UsersList,GroupsList,


#Color characters
COLORS = {
            'red'        : '\x1b[31;01m',
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
            'normal'     : '\x1b[0m'
         }

USE_COLOR = True
GUDEV_HANDLE = None

ACTIVATED, DEACTIVATED = range(2)

def colorize(msg, color):
    """Colorize the given message if requested."""
    if not USE_COLOR:
        return msg
    else:
        return "%s%s%s" % (COLORS[color], msg, COLORS['normal'])

def get_input(label):
    """Get input from the terminal."""
    try:
        return raw_input(colorize(("%s > " % label), 'light'))
    except (KeyboardInterrupt, EOFError):
        print
        sys.exit(1)

def get_number(label, min_, max_):
    """Get a number from the terminal."""
    index_ = min_ - 1
    while index_ < min_ or index_ > max_:
        try:
            index_ = int(raw_input(colorize(("%s > " % label), 'light')))
        except ValueError:
            pass
        except (KeyboardInterrupt, EOFError):
            print
            sys.exit(1)
    return index_




