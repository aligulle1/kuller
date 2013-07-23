#!/bin/bash

CHANNEL="release"
BRANCH="releases/comm-$CHANNEL"
RELEASE_TAG="THUNDERBIRD_10_0_2_RELEASE"
VERSION="10.0.2"

test ! -d thunderbird && mkdir thunderbird
hg clone http://hg.mozilla.org/$BRANCH thunderbird
pushd thunderbird
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd

tar cjf thunderbird-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS thunderbird

