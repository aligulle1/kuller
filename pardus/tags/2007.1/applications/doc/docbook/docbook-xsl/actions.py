#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    items = ['template', 'fo', 'xhtml', 'profiling', 'website', 'images',
             'html', 'params', 'htmlhelp', 'roundtrip', 'tools', 'highlighting',
             'slides', 'docsrc', 'eclipse', 'manpages', 'javahelp', 'extensions', 'common', 'lib']

    for item in items:
        pisitools.insinto("/usr/share/sgml/docbook/xsl-stylesheets-1.72.0/%s" % item, "%s/*" % item)

    pisitools.insinto("/usr/share/sgml/docbook/xsl-stylesheets-1.72.0", "VERSION")

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README", "RELEASE-NOTES.txt", "TODO", "VERSION")
