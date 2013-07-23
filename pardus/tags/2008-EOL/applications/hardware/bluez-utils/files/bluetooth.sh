#!/bin/bash

# Ignore this request as dbus has not been started yet.
if [ ! -S /var/run/dbus/system_bus_socket ]; then
    exit 1
fi

# It is really not necessary to stop it, it's just a little daemon..

case $ACTION in
    add)
        service bluez_utils start
        ;;

#    remove)
#        service bluez_utils stop
#        ;;

    *)
        exit 1
        ;;
esac

