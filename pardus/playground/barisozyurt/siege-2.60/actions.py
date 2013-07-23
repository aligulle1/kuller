from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--with-ssl")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README.https")

