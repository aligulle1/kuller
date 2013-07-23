#!/bin/bash

is_true ()
{
  [ "$1" = "y" -o "$1" = "Y" -o "$1" = "yes" -o "$1" = "YES" ]
}

start_serial() {
    service bluez-utils start

    IRQ=`setserial $DEVNAME | sed -e 's/.*IRQ: //'`
    setserial $DEVNAME irq 0 ; setserial $DEVNAME irq $IRQ

    DEVICE=`echo $DEVNAME|sed -e 's_/dev/__'`
    MANFID=`cat /$SYSFS/$PHYSDEVPATH/manf_id`","`cat /$SYSFS/$PHYSDEVPATH/card_id`
    # I don't have a generic solution, sorry
    if [ $MANFID = "0x0160,0x0002" ]; then
        /usr/sbin/hciattach $DEVICE $MANFID 115200
    else
        /usr/sbin/hciattach $DEVICE $MANFID
    fi
}

stop_serial() {
    service bluez-utils stop
    is_true $NO_FUSER && return 1
    fuser -k -HUP $DEVNAME > /dev/null
}

case "$ACTION" in
  add)
    start_serial
    ;;
  remove)
    stop_serial
    ;;
  *)
    exit 1
    ;;
esac
