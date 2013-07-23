#!/bin/bash

case $ACTION in
    add)
        service bluez-utils start
        ;;

    remove)
        service bluez-utils stop
        ;;

    *)
        exit 1
        ;;
esac

