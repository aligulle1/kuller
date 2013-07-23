#!/usr/bin/python

import os
import grp
import pwd
import glob
import shutil

def uniq(alist):
    set = {}
    return [set.setdefault(e,e) for e in alist if e not in set]

def postInstall():
    # We don't want to overwrite an existing file during upgrade
    specialFiles = ["hosts", "passwd", "shadow", "group", "fstab", "ld.so.conf", "resolv.conf"]

    for specialFile in specialFiles:
        if not os.path.exists("/etc/%s" % specialFile):
            shutil.copy("/usr/share/baselayout/%s" % specialFile, "/etc")

    shutil.copy("/etc/passwd", "/usr/share/baselayout/passwd.backup")
    shutil.copy("/etc/group", "/usr/share/baselayout/group.backup")

    # build user -> group map for migration
    migration = []
    for user in pwd.getpwall():
        groups = []
        if user[2] >= 1000 and user[2] < 65534:
            for group in grp.getgrall():
                if group[3].__contains__(user[0]):
                    groups.append(group[0])
            if groups.__contains__("cdrom"):
                groups.remove("cdrom")
                groups.append("removable")
            if groups.__contains__("plugdev"):
                groups.remove("plugdev")
                groups.append("removable")

            if groups.__contains__("lp"):
                groups.remove("lp")
                groups.append("pnp")
            if groups.__contains__("scanner"):
                groups.remove("scanner")
                groups.append("pnp")
            if len(groups) > 0:
                migration.append("hav call User.Manager.setUser uid %s groups %s" % (user[2], ",".join(uniq(groups))))

        # Remove old groups/users
    groups = ["lp", "floppy", "uucp", "cdrom", "squid", "gdm", "xfs", "games", \
                "named", "mysql", "postgres", "cdrw", "apache", "nut", "usb", \
                "vpopmail", "users", "nofiles", "qmail", "postfix", "postdrop", "smmsp", \
                "slocate", "utmp", "scanner", "messagebus", "haldaemon", "plugdev", "firebird", \
                "dhcp", "ntlmaps", "ldap", "clamav"]

    for group in groups:
        try:
            gid = grp.getgrnam(group)[2]
            os.system("hav call User.Manager.deleteGroup gid %s" % gid)
        except KeyError:
            pass

    users = ["lp", "uucp", "squid", "gdm", "xfs", "games", \
                "named", "mysql", "postgres", "apache", "nut", "cyrus", \
                "vpopmail", "messagebus", "haldaemon", "alias", "qmaild", "qmaill", \
                "qmailp", "qmailq", "qmailr", "qmails", "postfix", "smmsp", "firebird", \
                "dhcp", "ntlmaps", "ldap", "clamav"]

    for user in users:
        try:
            uid = pwd.getpwnam(user)[2]
            os.system("hav call User.Manager.deleteUser uid %s" % uid)
        except KeyError:
            pass

    # Merge new system groups
    # I will replace these with proper comar calls, after finishing
    # some comar api work there, right now they are ok
    os.system("hav call User.Manager.addGroup gid 50 name named")
    os.system("hav call User.Manager.addGroup gid 60 name mysql")
    os.system("hav call User.Manager.addGroup gid 70 name postgres")
    os.system("hav call User.Manager.addGroup gid 80 name apache")
    os.system("hav call User.Manager.addGroup gid 90 name dovecot")
    os.system("hav call User.Manager.addGroup gid 100 name users")
    os.system("hav call User.Manager.addGroup gid 101 name dbus")
    os.system("hav call User.Manager.addGroup gid 102 name hal")
    os.system("hav call User.Manager.addGroup gid 103 name polkit")
    os.system("hav call User.Manager.addGroup gid 104 name postfix")
    os.system("hav call User.Manager.addGroup gid 105 name postdrop")
    os.system("hav call User.Manager.addGroup gid 106 name smmsp")
    os.system("hav call User.Manager.addGroup gid 107 name slocate")
    os.system("hav call User.Manager.addGroup gid 108 name utmp")
    os.system("hav call User.Manager.addGroup gid 109 name firebird")
    os.system("hav call User.Manager.addGroup gid 110 name dhcp")
    os.system("hav call User.Manager.addGroup gid 111 name ldap")
    os.system("hav call User.Manager.addGroup gid 112 name clamav")
    os.system("hav call User.Manager.addGroup gid 113 name ntlmaps")
    os.system("hav call User.Manager.addGroup gid 123 name ntp")
    # Comar' profile groups
    os.system("hav call User.Manager.addGroup gid 200 name pnp")
    os.system("hav call User.Manager.addGroup gid 201 name removable")
    os.system("hav call User.Manager.addGroup gid 202 name netuser")
    os.system("hav call User.Manager.addGroup gid 203 name netadmin")
    os.system("hav call User.Manager.addGroup gid 204 name power")
    os.system("hav call User.Manager.addGroup gid 205 name pnpadmin")

    # Merge new system users
    os.system("hav call User.Manager.addUser uid 40 name named realname Bind shell /bin/false homedir /var/bind groups named")
    os.system("hav call User.Manager.addUser uid 60 name mysql realname MySQL shell /bin/false homedir /var/lib/mysql groups mysql")
    os.system("hav call User.Manager.addUser uid 70 name postgres realname PostgreSQL shell /bin/bash homedir /var/lib/postgresql groups postgres")
    os.system("hav call User.Manager.addUser uid 80 name apache realname Apache shell /bin/false homedir /dev/null groups apache")
    os.system("hav call User.Manager.addUser uid 90 name dovecot realname Dovecot shell /bin/false homedir /dev/null groups dovecot")
    os.system("hav call User.Manager.addUser uid 101 name dbus realname D-BUS shell /bin/false homedir /dev/null groups dbus")
    os.system("hav call User.Manager.addUser uid 102 name hal realname Hal shell /bin/false homedir /dev/null groups hal")
    os.system("hav call User.Manager.addUser uid 103 name polkit realname PolicyKit shell /bin/false homedir /dev/null groups polkit")
    os.system("hav call User.Manager.addUser uid 104 name postfix realname Postfix shell /bin/false homedir /var/spool/postfix groups postfix")
    os.system("hav call User.Manager.addUser uid 106 name smmsp realname smmsp shell /bin/false homedir /var/spool/mqueue groups smmsp")
    os.system("hav call User.Manager.addUser uid 109 name firebird realname Firebird shell /bin/false homedir /opt/firebird groups firebird")
    os.system("hav call User.Manager.addUser uid 110 name dhcp realname DHCP shell /bin/false homedir /dev/null groups dhcp")
    os.system("hav call User.Manager.addUser uid 111 name ldap realname OpenLDAP shell /bin/false homedir /dev/null groups ldap")
    os.system("hav call User.Manager.addUser uid 112 name clamav realname Clamav shell /bin/false homedir /dev/null groups clamav")
    os.system("hav call User.Manager.addUser uid 113 name ntlmaps realname NTLMaps shell /bin/false homedir /dev/null groups ntlmaps")
    os.system("hav call User.Manager.addUser uid 123 name ntp realname NTP shell /bin/false homedir /dev/null groups ntp")
    # Comar' profile users
    os.system("hav call User.Manager.addUser uid 200 name pnp realname PnP shell /bin/false homedir /dev/null groups pnp")

    #migrate
    for cmd in migration:
        os.system(cmd)

    # We should only install empty files if these files don't already exist.
    if not os.path.exists("/var/log/lastlog"):
        os.system("/usr/bin/touch /var/log/lastlog")
    if not os.path.exists("/var/run/utmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/run/utmp")
    if not os.path.exists("/var/log/wtmp"):
        os.system("/usr/bin/install -m 0664 -g utmp /dev/null /var/log/wtmp")

    # Enable shadow groups
    os.system("/usr/sbin/grpconv")
    os.system("/usr/sbin/grpck -r &>/dev/null")

    # Create /root if not exists
    if not os.path.exists("/root/"):
        shutil.copytree("/etc/skel", "/root")
        os.chown("/root", 0, 0)
        os.chmod("/root", 0700)

    # Tell init to reload new inittab
    os.system("/sbin/telinit q")

    # Skype language selector
    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]

    if lang == "tr_TR":
        os.system("sed -i -e 's/<Language>.*<\/Language>/<Language>tr<\/Language>/' /etc/skel/.Skype/shared.xml")
    elif lang == "nl_NL":
        os.system("sed -i -e 's/<Language>.*<\/Language>/<Language>nl<\/Language>/' /etc/skel/.Skype/shared.xml")
    elif lang == "de_DE":
        os.system("sed -i -e 's/<Language>.*<\/Language>/<Language>de<\/Language>/' /etc/skel/.Skype/shared.xml")
    elif lang == "es_ES":
        os.system("sed -i -e 's/<Language>.*<\/Language>/<Language>es<\/Language>/' /etc/skel/.Skype/shared.xml")
    else:
        os.system("sed -i -e 's/<Language>.*<\/Language>/<Language>en<\/Language>/' /etc/skel/.Skype/shared.xml")
