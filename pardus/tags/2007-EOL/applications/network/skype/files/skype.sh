#!/bin/bash
#
progname="skype"
progpath="/opt/${progname}/"
progopts="--resources-path ${progpath}"

cd ${progpath}
skypecmd="${progpath}${progname}"
exec ${skypecmd} ${progopts} $@
