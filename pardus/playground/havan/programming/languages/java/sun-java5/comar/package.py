#!/usr/bin/python

import os

def postInstall():

        # Create files used as storage for system preferences.
        PREFS_LOCATION = "/opt/sun-java5-jdk/jre"

        try:
            os.makedirs("%s/.systemPrefs" % PREFS_LOCATION)
        except OSError:
            pass

        if not os.path.exists("%s/.systemPrefs/.system.lock" % PREFS_LOCATION):
                os.system("/usr/bin/touch %s/.systemPrefs/.system.lock" % PREFS_LOCATION)
                os.system("/usr/bin/chmod 644 %s/.systemPrefs/.system.lock" % PREFS_LOCATION)

        if not os.path.exists("%s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION):
                os.system("/usr/bin/touch %s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION)
                os.system("/usr/bin/chmod 644 %s/.systemPrefs/.systemRootModFile" % PREFS_LOCATION)
