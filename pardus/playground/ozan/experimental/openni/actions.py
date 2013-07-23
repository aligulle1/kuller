# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "OpenNI-OpenNI-4dbf64b"

def setup():
    shelltools.chmod("Platform/Linux/CreateRedist/RedistMaker", 0755)
    shelltools.system("rm -rf Samples/*/GL Samples/*/Libs Source/External Platform/Linux/Build/Prerequisites/*")
    shelltools.system("dos2unix *.txt README")

    pisitools.dosed("Samples/*/*.c", "^#define SAMPLE_XML_PATH .*$", "#define SAMPLE_XML_PATH \"/etc/openni/SamplesConfig.xml\"")
    pisitools.dosed("Samples/*/*.cpp", "^#define SAMPLE_XML_PATH .*$", "#define SAMPLE_XML_PATH \"/etc/openni/SamplesConfig.xml\"")

def build():
    shelltools.cd("Platform/Linux/CreateRedist")
    shelltools.system("DEBUG=1 ./RedistMaker")

def install():
    # Samples
    for sample in ("NiAudioSample", "NiBackRecorder",
                   "NiConvertXToONI", "NiCRead", "NiRecordSynthetic",
                   "NiSimpleCreate", "NiSimpleRead", "NiSimpleViewer",
                   "NiUserTracker"):
        pisitools.insinto("/usr/bin", "Platform/Linux/Bin/x64-Release/Sample-%s" % sample, sample)

    pisitools.insinto("/usr/lib", "Platform/Linux/Bin/x64-Release/libSample-NiSampleModule.so", "libNiSampleModule.so")
    pisitools.insinto("/usr/bin", "Platform/Linux/Bin/x64-Release/NiViewer")

    # Documentation
    pisitools.dodoc("*.txt", "README", "Documentation/*.pdf")
    pisitools.dohtml("Source/DoxyGen/html/*")

    pisitools.insinto("/etc/openni", "Data/SamplesConfig.xml")

    shelltools.cd("Platform/Linux/Redist/OpenNI-Bin-Dev-Linux-x64-v%s" % get.srcVERSION())
    shelltools.system("INSTALL_LIB=%s/usr/lib INSTALL_BIN=%s/usr/bin \
               INSTALL_INC=%s/usr/include/ni INSTALL_VAR=%s/var/lib/ni \
               INSTALL_JAR=%s/usr/lib/openni ./install.sh -n" % ((get.installDIR(),)*5))

