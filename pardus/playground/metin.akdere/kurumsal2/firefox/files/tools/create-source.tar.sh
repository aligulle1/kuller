#!/bin/bash

BRANCH="releases/mozilla-release"
RELEASE_TAG="FIREFOX_7_0_RELEASE"
VERSION="7.0"

test ! -d release-src && hg clone http://hg.mozilla.org/$BRANCH release-src
pushd release-src
hg push
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd
tar cjf firefox-source-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS release-src

