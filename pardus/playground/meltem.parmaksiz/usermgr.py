# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2009 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#

import os
import glob
import time
import fcntl
import random
import shutil
import hashlib
import libuser

from string import ascii_letters, digits

#import python-polkit bindings
import polkit

#libuser initializing
admin = libuser.admin()

# faces
FACES = [
    "/usr/kde/4/share/apps/kdm/pics/users",
]

def setFace(uid, homedir):
    files = []
    for directory in FACES:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if filename.endswith(".png"):
                    files.append(os.path.join(directory, filename))
    if len(files):
        icon = os.path.join(homedir, ".face.icon")
        shutil.copy(random.choice(files), icon)
        os.chmod(icon, 0644)
        os.chown(icon, uid, 100)

#methods

def userList():
    user_list = []

    users = admin.enumerateUsersFull()
    for user in users:
        user_list.append((int(user[libuser.UIDNUMBER][0]), user[libuser.USERNAME][0], user[libuser.GECOS][0]))

    return user_list

def userInfo(uid):
#    try:
    user = admin.lookupUserById((uid))
    ret=(
        user[libuser.USERNAME],
        user.get(libuser.GECOS),
        user.get(libuser.GIDNUMBER),
        user.get(libuser.HOMEDIRECTORY),
        user.get(libuser.LOGINSHELL),
        user.get(libuser.GROUPNAME),
#                    admin.lookupGroupById(int(user[libuser.GIDNUMBER][1]))[libuser.GROUPNAME]
        )
#    except Exception,e:
#        fail(e)

    return ret

def addUser(uid, name, realname, homedir, shell, password, groups, grants, blocks):
    new_user = admin.initUser(name)

    if not uid == -1:
        new_user.set(libuser.UIDNUMBER, uid)
    if realname:
        new_user.set(libuser.GECOS, realname)
    if homedir:
        new_user.set(libuser.HOMEDIRECTORY, homedir)
    if shell:
        new_user.set(libuser.LOGINSHELL, shell)
    if password:
        new_user.set(libuser.SHADOWPASSWORD, shadowCrypt(password))
    if groups:
        new_user.set(libuser.GROUPNAME, groups)

    for grant in grants:
        if grant != "":
            grantAuthorization(uid, grant)
    for block in blocks:
        if block != "":
            blockAuthorization(uid, block)
    try:
        admin.addUser(new_user)
    except Exception, e:
        fail(e)

    new_user = admin.lookupUserByName(name)
#    setFace(new_user[libuser.UIDNUMBER][0], new_user[libuser.HOMEDIRECTORY][0])
    return new_user[libuser.UIDNUMBER][0]

def setUser(uid, realname, homedir, shell, password, groups):
    try:
        user = admin.lookupUserById(int(uid))
        if user:
            if realname:
                user.set(libuser.GECOS, realname)
            if homedir:
                user.set(libuser.HOMEDIRECTORY, homedir)
            if shell:
                user.set(libuser.LOGINSHELL, shell)
            if password:
                user.set(libuser.SHADOWPASSWORD, shadowCrypt(password))
            if groups:
                user.set(libuser.GROUPNAME, name)
        admin.modifyUser(user)
    except Exception, e:
        fail(e)


def deleteUser(uid, deletefiles):
    user = admin.lookupUserById(int(uid))
    admin.deleteUser(user)
    admin.removeHome(user)


def groupList():
    group_list=[]

    groups = admin.enumerateGroupsFull()
    for group in groups:
        group_list.append((int(group[libuser.GIDNUMBER][0]), group[libuser.GROUPNAME][0]))

    return group_list

def addGroup(gid, name):
    new_group = admin.initGroup(name)

    if not gid == -1:
        new_group[libuser.GIDNUMBER] = gid

    try:
        admin.addGroup(new_group)
    except Exception, e:
        fail(e)

    group = admin.lookupGroupByName(gid)
    return group[libuser.UIDNUMBER][0]

def deleteGroup(gid):
    group = admin.lookupGroupById(int(gid))
    admin.deleteGroup(group)


#
# Crypt function for shadow file
#

def shadowCrypt(password):
    des_salt = list('./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    salt, magic = str(random.random())[-8:], '$1$'

    ctx = hashlib.md5(password)
    ctx.update(magic)
    ctx.update(salt)

    ctx1 = hashlib.md5(password)
    ctx1.update(salt)
    ctx1.update(password)

    final = ctx1.digest()

    for i in range(len(password), 0 , -16):
        if i > 16:
            ctx.update(final)
        else:
            ctx.update(final[:i])

    i = len(password)

    while i:
        if i & 1:
            ctx.update('\0')
        else:
            ctx.update(password[:1])
        i = i >> 1
    final = ctx.digest()

    for i in range(1000):
        ctx1 = hashlib.md5()
        if i & 1:
            ctx1.update(password)
        else:
            ctx1.update(final)
        if i % 3: ctx1.update(salt)
        if i % 7: ctx1.update(password)
        if i & 1:
            ctx1.update(final)
        else:
            ctx1.update(password)
        final = ctx1.digest()

    def _to64(v, n):
        r = ''
        while (n-1 >= 0):
            r = r + des_salt[v & 0x3F]
            v = v >> 6
            n = n - 1
        return r

    rv = magic + salt + '$'
    final = map(ord, final)
    l = (final[0] << 16) + (final[6] << 8) + final[12]
    rv = rv + _to64(l, 4)
    l = (final[1] << 16) + (final[7] << 8) + final[13]
    rv = rv + _to64(l, 4)
    l = (final[2] << 16) + (final[8] << 8) + final[14]
    rv = rv + _to64(l, 4)
    l = (final[3] << 16) + (final[9] << 8) + final[15]
    rv = rv + _to64(l, 4)
    l = (final[4] << 16) + (final[10] << 8) + final[5]
    rv = rv + _to64(l, 4)
    l = final[11]
    rv = rv + _to64(l, 2)

    return rv

#
# List authorizations by UID
#

def listUserAuthorizations(uid):
    actions = polkit.auth_list_uid(int(uid))
    auths = []
    for action in actions:
        action_info = polkit.action_info(action['action_id'])
        auths.append((action['action_id'], action['scope'], action_info['description'], action_info['policy_active'], action['negative']))
    return auths

#
# Grant authorization to user
#

def grantAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_add(action_id, polkit.SCOPE_ALWAYS, uid)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_add(action, polkit.SCOPE_ALWAYS, uid)
        except:
            return False
    return True

#
# Revoke authorization of user
#

def revokeAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
        except:
            return False
    return True

#
# Block authorization of user
#

def blockAuthorization(uid, action):
    uid = int(uid)
    if action == "*":
        for action_id in polkit.action_list():
            try:
                polkit.auth_revoke(uid, action_id)
                polkit.auth_block(uid, action_id)
            except:
                return False
    else:
        try:
            polkit.auth_revoke(uid, action)
            polkit.auth_block(uid, action)
        except:
            return False
    return True
