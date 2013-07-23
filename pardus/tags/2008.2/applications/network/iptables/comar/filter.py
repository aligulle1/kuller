import os
import os.path
import subprocess

import pardus.netfilterutils as iptables

CONFIG_PROFILE = "/etc/iptables/profile"
CONFIG_FILTER = "/etc/iptables/filter"
CONFIG_NAT = "/etc/iptables/nat"
CONFIG_MANGLE = "/etc/iptables/mangle"
CONFIG_RAW = "/etc/iptables/raw"

def writeFile(filename, content="", mode=0600):
    """Writes content to filename and set file mode."""
    file(filename, "w").write(content)
    os.chmod(filename, mode)

def readFile(filename):
    """Return content of a file"""
    return file(filename, "r").read()

def runProc(cmd):
    return subprocess.call(cmd.split())

def setRule(rule):
    state = call(script(), "System.Service", "info")[2]
    if state in ["off", "stopped"]:
        fail("FW is offline")

    ret = runProc("/sbin/iptables %s" % rule)
    if ret != 0:
        fail("Invalid rule")

def setProfile(profile, save_filter="", save_mangle="", save_nat="", save_raw=""):
    """Set FW profile."""

    writeFile(CONFIG_PROFILE, profile)
    writeFile(CONFIG_FILTER, save_filter)
    writeFile(CONFIG_NAT, save_filter)
    writeFile(CONFIG_MANGLE, save_mangle)
    writeFile(CONFIG_NAT, save_nat)

    notify("Net.Filter", "ProfileChanged", (profile, save_filter, save_mangle, save_nat, save_raw))

def getProfile():
    """Get FW profile."""
    config = []

    config_files = [
        (CONFIG_PROFILE, "profile"),
        (CONFIG_FILTER, "save_filter"),
        (CONFIG_NAT, "save_nat"),
        (CONFIG_MANGLE, "save_mangle"),
        (CONFIG_RAW, "save_raw"),
    ]

    for _file, _key in config_files:
        try:
            content = readFile(_file).strip()
        except IOError:
            content = ""
        if _key == "profile" and not len(content):
            content = "default"
        config.append(content)

    return tuple(config)

def getRules():
    """Get user defined rules."""
    state = call(script(), "System.Service", "info")[2]
    if state in ["off", "stopped"]:
        fail("FW is offline")

    profile, save_filter, save_nat, save_mangle, save_raw = getProfile()
    save = {
        "filter": save_filter,
        "nat": save_nat,
        "mangle": save_mangle,
        "raw": save_raw,
    }

    profile_file = os.path.join("/var/lib/iptables/", profile)

    base = {}
    changes = {}
    allowed_chains = {}

    for table in iptables.chains:
        allowed_chains[table] = save[table].split()

    # Get base rules from /var/lib/iptables/<profile>
    if os.path.isfile(profile_file):
        rules = file(profile_file).read()
        base = iptables.parseConf(rules)

    changes = iptables.parseConf(iptables.getRules())

    # Get user defined rules in filter table
    diff = iptables.filterDict(iptables.diffDict(changes, base), allowed_chains)

    ret = []
    for table in diff:
        for rule in diff[table]:
            ret.append("%s %s" % (table, rule))
    return ret
