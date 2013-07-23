#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
import re
import locale
from comar import Link
from sys import exit

uid = os.getuid()

if uid != 0:
    print "You need to run this script as root.\nExiting."
    exit()

warningmsg = "This script will create initial database entries for zoneminder server.\n\n\
 Note: if you're upgrading from an older version of zoneminder, instead of this script, use following command manually:\n\
 /usr/bin/zmupdate.pl version=<from version> [--user=<my_database_user> --pass=<my_database_pass>]\n\n\
Please make sure of there are no existing zoneminder database in the mysql instance!"


yesexpr = re.compile(locale.nl_langinfo(locale.YESEXPR))
print warningmsg
prompt = "continue? (yes/no): "
s = raw_input(prompt.encode('utf-8'))

if yesexpr.search(s) == None:
    print "Aborted."
    exit()

username = raw_input("Enter a valid mysql username: [root] ")

if username == "":
    username = "root"

print "Creating initial database entries for zoneminder:"

link = Link()
link.System.Service["mysql_server"].start()

command="mysql -u %s -p zm < /usr/share/zoneminder/db/zm_create.sql" % username
command2="mysql -u %s -p zm < /usr/share/zoneminder/db/zmuser.sql" % username

for cmd in [command, command2]:

    print "\nPlease enter mysql password for '%s' below" % username
    os.system(cmd)

exit()

