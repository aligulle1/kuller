#!/usr/bin/python

import os

def symlink(src, dest):
    try:
        os.symlink(src, dest)
    except OSError:
        pass

def postInstall():
    os.environ["HOME"] = "/root"
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/compreg.dat")
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/components/xpti.dat")
    os.system("/usr/lib/MozillaFirefox/firefox -register")
    os.system("/usr/bin/touch /usr/lib/MozillaFirefox/.autoreg")
    #FIXME: os.system("/usr/lib/MozillaFirefox/regxpcom")

    # Bookmarks/MimeTypes
    lang = open("/etc/env.d/03locale").readline().strip("LANG=")[:5]

    if lang == "tr_TR":
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-tr.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_tr.src", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.src")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_tr.src", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.src")
    elif lang == "nl_NL":
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-nl.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_nl.src", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.src")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_nl.src", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.src")
    elif lang == "pt_BR":
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_pt.src", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.src")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_pt.src", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.src")
    else:
        symlink("/usr/lib/MozillaFirefox/pardus/bookmarks-en.html", "/usr/lib/MozillaFirefox/defaults/profile/bookmarks.html")
        symlink("/usr/lib/MozillaFirefox/pardus/pardus-wiki_en.src", "/usr/lib/MozillaFirefox/searchplugins/pardus-wiki.src")
        symlink("/usr/lib/MozillaFirefox/pardus/wikipedia_en.src", "/usr/lib/MozillaFirefox/searchplugins/wikipedia.src")

def preRemove():
    try:
        os.unlink("/usr/lib/MozillaFirefox/.autoreg")
    except OSError:
        pass
