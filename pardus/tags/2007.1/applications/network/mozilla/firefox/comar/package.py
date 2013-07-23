#!/usr/bin/python

import os

def postInstall():
    os.environ["HOME"] = "/root"
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/compreg.dat")
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/xpti.dat")
    os.system("/usr/lib/MozillaFirefox/firefox -register")
    #FIXME: os.system("/usr/lib/MozillaFirefox/regxpcom")

    # Bookmarks/MimeTypes
    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]

    try:
        if lang == "tr_TR":
            os.symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-tr.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        elif lang == "nl_NL":
            os.symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-nl.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        else:
            os.symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-en.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
    except OSError:
        pass
