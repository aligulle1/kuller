from comar.service import *
import sys
from subprocess import Popen,PIPE

serviceType="server"
serviceDesc = _({"en": "Bridged Network Creation Service",
                 "tr": "Köprülenmiş Ağ Bağlantısı Yaratma Servisi"})

# For more detailed information on usage, please read the README file in /usr/share/doc

@synchronized
def start():
    # Check if the service is already running
    if status() == True:
        fail("Service is already running...")

    # Read configuration file, use int() function to convert the string value to numeric value
    DEVICE_NAME=config.get("DEVICE_NAME", "")
    NUMBER_OF_DEVICES=int((config.get("NUMBER_OF_DEVICES", "")))
    BRIDGE_NAME=config.get("BRIDGE_NAME", "")
    PHYSICAL_INTF_TO_BRIDGE=config.get("PHYSICAL_INTF_TO_BRIDGE", "")
    CONNECTION_NAME=config.get("CONNECTION_NAME", "")

    # Use this simple variable to store return values to detect errors
    ret=0

    # create required number of tap devices within group "tun" with the name DEVICE_NAME
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/usr/bin/tunctl -g wheel -t %s%s" % (DEVICE_NAME, i))

    # use ifconfig to enable the tap devices created above
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/sbin/ifconfig %s%s up" % (DEVICE_NAME, i))

    # Create the bridge with the name "BRIDGE_NAME"
    ret += os.system("/usr/sbin/brctl addbr %s" % BRIDGE_NAME)

    # add the previously created tap devices to the bridge
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/usr/sbin/brctl addif %s %s%s" % (BRIDGE_NAME, DEVICE_NAME, i))

    # check if user requests physical device to be included in the bridge, add if device name given
    if PHYSICAL_INTF_TO_BRIDGE != "disabled":
        ret += os.system("/sbin/ifconfig %s 0.0.0.0 promisc up" % PHYSICAL_INTF_TO_BRIDGE)
        ret += os.system("/usr/sbin/brctl addif %s %s" % (BRIDGE_NAME, PHYSICAL_INTF_TO_BRIDGE))

    # enable the bridge and use network command to bring up the network connection
    ret += run("/sbin/ifconfig %s up" % BRIDGE_NAME)

    if CONNECTION_NAME != "disabled":
        run("/bin/network up %s" % CONNECTION_NAME)

    # Check if everything went right, warn user if there was an error
    if ret == 0:
       notify("System.Service", "Changed", "started")
    else:
       fail("An error occured while starting service, please check configuration file and your network configuration.")

@synchronized
def stop():

    # Check if the service is running before trying to stop it
    if status() == False:
        fail("Service is not running...")

    # Read configuration file, use int() function to convert the string value to numeric value
    DEVICE_NAME=config.get("DEVICE_NAME", "")
    NUMBER_OF_DEVICES=int((config.get("NUMBER_OF_DEVICES", "")))
    BRIDGE_NAME=config.get("BRIDGE_NAME", "")
    PHYSICAL_INTF_TO_BRIDGE=config.get("PHYSICAL_INTF_TO_BRIDGE", "")
    CONNECTION_NAME=config.get("CONNECTION_NAME", "")

    # Use this simple variable to store return values to detect errors
    ret=0

    if CONNECTION_NAME != "disabled":
        run("/bin/network down %s" % CONNECTION_NAME)

    # disable the network bridge from network configuration
    ret += os.system("/sbin/ifconfig %s down" % BRIDGE_NAME)

    # check if the physical interface was included in the bridge, remove if it was
    if PHYSICAL_INTF_TO_BRIDGE != "disabled":
        ret += os.system("/usr/sbin/brctl delif %s %s" % (BRIDGE_NAME, PHYSICAL_INTF_TO_BRIDGE))
        ret += os.system("/sbin/ifconfig %s down" % PHYSICAL_INTF_TO_BRIDGE)

    # remove tap devices from the bridge
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/usr/sbin/brctl delif %s %s%s" % (BRIDGE_NAME, DEVICE_NAME, i))

    # delete the bridge
    ret += run("/usr/sbin/brctl delbr %s" % BRIDGE_NAME)

    # disable tap devices from network configuration
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/sbin/ifconfig %s%s down" % (DEVICE_NAME, i))

    # completely remove network devices
    for i in range(0, NUMBER_OF_DEVICES):
        ret += os.system("/usr/bin/tunctl -d %s%s" % (DEVICE_NAME, i))

    # Check if everything went right, warn user if there was an error
    if ret == 0:
        notify("System.Service", "Changed", "stopped")
    else:
        fail("An error occured while stopping service, please check your network configuration.")

def status():

    # function works by checking if the named bridge adapter is up and running on the system
    # read the name of the bridge to be checked
    BRIDGE_NAME=config.get("BRIDGE_NAME", "")

    # get the output of ifconfig command. This command alone gives only interfaces which are UP
    p1 = Popen(["/sbin/ifconfig"], stdout=PIPE)
    # filter the output to see if it includes our bridge name
    p2 = Popen(["/bin/grep", "%s" % BRIDGE_NAME], stdin=p1.stdout, stdout=PIPE)
    # get the first word
    output = p2.communicate()[0].split(" ")[0]

    # compare the first word from output with the name of our bridge, return True if they match
    return BRIDGE_NAME == output
