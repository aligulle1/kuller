#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pwd

settings_file = ".macromedia/Flash_Player/macromedia.com/support/flashplayer/sys/settings.sol"

safe_config = '\x00\xbf\x00\x00\x01;TCSO\x00\x04\x00\x00\x00\x00\x00\x08settings\x00\x00\x00\x00\x00\x04gain\x00@I\x00\x00\x00\x00\x00\x00\x00\x00\x0fechosuppression\x01\x00\x00\x00\x11defaultmicrophone\x02\x00\x00\x00\x00\rdefaultcamera\x02\x00\x00\x00\x00\rdefaultklimit\x00@Y\x00\x00\x00\x00\x00\x00\x00\x00\rdefaultalways\x01\x00\x00\x00\x11windowlessDisable\x01\x00\x00\x00\x10crossdomainAllow\x01\x00\x00\x00\x11crossdomainAlways\x01\x00\x00\x00\x1asecureCrossDomainCacheSize\x00\xbf\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x18allowThirdPartyLSOAccess\x01\x01\x00\x00\x0ctrustedPaths\x03\x00\x00\t\x00\x00\x0esafefullscreen\x01\x01\x00'

def enable_safefullscreen(path):

    f = open(path, "rb+")
    data = f.read()
    f.seek(data.index('safefullscreen') + len('safefullscreen') + 1)
    f.write('\x01')
    f.close()

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    users = {}
    for dir in [d for d in os.listdir('/home') if os.path.isdir('/home/%s' % d)]:
        try:
            # Store the users having a passwd entry
            users[dir] = pwd.getpwnam(dir)
        except KeyError:
            pass

    for u in users.keys():
        # Modify the existing configuration file or create a new one if it doesn't exist
        file_path = '/home/%s/%s' % (u, settings_file)
        try:
            if os.path.exists(file_path):
                enable_safefullscreen(file_path)
            else:
                # Create the directory
                os.makedirs(os.path.dirname(file_path))

                # Create it and chown it correctly
                open(file_path, 'wb').write(safe_config)

                os.system("/bin/chown -R %d:%d /home/%s/.macromedia" % (users[u][2], users[u][3], u))
        except:
            pass
