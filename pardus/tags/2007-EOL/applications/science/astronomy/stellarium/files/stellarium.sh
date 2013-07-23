#!/bin/sh

# Wrapper script or stellarium. It has initialization problems with tr_TR.UTF-8 locale.
# You can change the language of programme by clicking configuration window inside it

LC_ALL=en_US.UTF-8 stellarium $1
