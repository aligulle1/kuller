#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    for data in ['*.el', 'ecb-images', 'html-help', 'info-help', 'Makefile']:
        pisitools.insinto('/usr/share/emacs/site-lisp/ecb/', data)
