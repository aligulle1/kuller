#/usr/bin/python

import os

def postInstall():
    # Remove zemberek, after Pardus 2007 Beta1 we install it at first run
    os.system("/opt/OpenOffice.org/lib/ooo-2.0/program/unopkg remove zemberek.zip")

    # Clean up past mistakes
    try:
        os.unlink("/opt/OpenOffice.org/lib/ooo-2.0/share/registry/data/org/openoffice/Office/Linguistic.xcu")
    except OSError:
        pass
