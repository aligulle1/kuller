#!/bin/sh
#
# Customized agents shutdown file
#
GPG_PID=`pidof gpg-agent`
if test -n "$GPG_PID"; then
    kill -9 $GPG_PID
fi

SSH_PID=`pidof ssh-agent`
if test -n "$SSH_PID"; then
    kill -9 $SSH_PID
fi
