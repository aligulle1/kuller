#!/bin/bash

CHANNEL="release"
BRANCH="releases/comm-$CHANNEL"
RELEASE_TAG="THUNDERBIRD_9_0_1_RELEASE"
VERSION="9.0.1"

test ! -d thunderbird && mkdir thunderbird
hg clone http://hg.mozilla.org/$BRANCH thunderbird
pushd thunderbird
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd

tar cjf thunderbird-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS thunderbird

