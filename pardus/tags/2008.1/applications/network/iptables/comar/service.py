from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Firewall",
                 "tr": "Güvenlik Duvarı"})

lock_file = "/var/lock/subsys/iptables"

import os
import pardus.netfilterutils as iptables

CONFIG_PROFILE = "/etc/iptables/profile"
CONFIG_FILTER = "/etc/iptables/filter"
CONFIG_NAT = "/etc/iptables/nat"
CONFIG_MANGLE = "/etc/iptables/mangle"
CONFIG_RAW = "/etc/iptables/raw"

def writeFile(filename, content="", mode=0600):
    '''Writes content to filename and set file mode.'''
    file(filename, "w").write(content)
    os.chmod(filename, mode)

def readFile(filename):
    """Return content of a file"""
    return file(filename, "r").read()

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

def stop():
    # Save rules
    profile, save_filter, save_nat, save_mangle, save_raw = getProfile()
    save = {
        "filter": save_filter,
        "nat": save_nat,
        "mangle": save_mangle,
        "raw": save_raw,
    }

    profile_file = os.path.join('/var/lib/iptables', profile)
    profile_changes = '%s.diff' % profile_file

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

    # Save allowed changes to /var/lib/iptables/<profile>.diff
    diff = iptables.filterDict(iptables.diffDict(changes, base), allowed_chains)

    writeFile(profile_changes, iptables.makeConf(diff))

    # Clear chains & rules
    iptables.clear()

    # Remove lock file
    if os.access(lock_file, os.F_OK):
        os.unlink(lock_file)

def start():
    # Clear chains & rules
    iptables.clear()

    # Load rules
    profile, save_filter, save_nat, save_mangle, save_raw = getProfile()
    save = {
        "filter": save_filter,
        "nat": save_nat,
        "mangle": save_mangle,
        "raw": save_raw,
    }

    profile_file = os.path.join('/var/lib/iptables', profile)
    profile_changes = '%s.diff' % profile_file

    base = {}
    changes = {}
    allowed_chains = {}

    for table in iptables.chains:
        allowed_chains[table] = save[table].split()

    # Load base rules
    if os.path.isfile(profile_file):
        rules = file(profile_file).read()
        base = iptables.parseConf(rules)
        iptables.restoreRules(rules)

    # Load allowed changes done in previous session
    if os.path.isfile(profile_changes):
        rules = file(profile_changes).read()
        changes = iptables.parseConf(rules)
        diff = iptables.filterDict(iptables.diffDict(changes, base), allowed_chains)
        iptables.restoreRules(iptables.makeConf(diff), flush=False)

    # Create lock file
    writeFile(lock_file, '')

def status():
    return os.access(lock_file, os.F_OK)
