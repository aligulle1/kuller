#!/bin/bash

set -e

PREFIX=/usr
CFLAGS="-mtune=generic -march=x86-64 -O2 -pipe -fomit-frame-pointer -fstack-protector -D_FORTIFY_SOURCE=2 -ggdb3 -funwind-tables -fasynchronous-unwind-tables"
CC="ccache gcc"
MAKE="make -j9"

COMMON_DEPS="jpeg-devel fontconfig-devel fribidi-devel librsvg-devel cairo-devel mesa-devel DirectFB-devel libXext-devel libXrender-devel giflib-devel freetype-devel tiff-devel libXcursor-devel libXdamage-devel libXcomposite-devel libXfixes-devel libXinerama-devel libXi-devel libXrandr-devel libXrender-devel libXScrnSaver-devel libXtst-devel lua-devel alsa-lib-devel xterm cython"
BUILD_E_DEPENDS="eeze"
BUILD_ETHUMB_DEPENDS="PROTO/epdf emotion"
BUILD_ELM_DEPENDS="PROTO/emap eio"
BUILD_BASIC="eina eet evas ecore embryo edje e_dbus efreet expedite "$BUILD_E_DEPENDS" e "$BUILD_ETHUMB_DEPENDS" ethumb "$BUILD_ELM_DEPENDS" elementary"
BUILD_PYTHON_BINDINGS="BINDINGS/python/python-evas BINDINGS/python/python-elementary BINDINGS/python/python-ecore BINDINGS/python/python-edje BINDINGS/python/python-emotion"
BUILD_BINDINGS=$BUILD_PYTHON_BINDINGS
BUILD_E_MODULES="E-MODULES-EXTRA/comp-scale E-MODULES-EXTRA/notification E-MODULES-EXTRA/engage E-MODULES-EXTRA/everything-shotgun E-MODULES-EXTRA/everything-pidgin"
BUILD_ETC="editje PROTO/eyelight ephoto edje_viewer PROTO/emap eio enjoy"
BUILD="$BUILD_BASIC $BUILD_BINDINGS $BUILD_E_MODULES $BUILD_ETC"

sudo pisi it $COMMON_DEPS

for I in $BUILD; do
  pushd $I
	echo " "
	echo "============ "$I" ============"
	$MAKE clean distclean || true
	./autogen.sh --prefix=/usr --disable-static --sysconfdir=/etc
	$MAKE
	sudo $MAKE install
	sudo ldconfig
  popd
done

echo ""
echo "============ detourious elm theme ============"
pushd THEMES/detourious/elm
    $MAKE
    $MAKE install
popd

#detourious
echo ""
echo "============ detourious ============"
pushd THEMES/detourious
	$MAKE
	$MAKE install
popd

enlightenment_remote -restart
