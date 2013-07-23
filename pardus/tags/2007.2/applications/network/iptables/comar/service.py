from comar.service import *
import os
import os.path

from iptables import *

serviceType = "local"
serviceDesc = _({"en": "Firewall",
                 "tr": "Güvenlik Duvarı"})


lock_file = '/var/run/iptables/iptables.lock'


def writeFile(filename, content, mode=0600):
    '''Writes content to filename and set file mode.'''
    f = file(filename, 'w')
    f.write(content)
    f.close()
    os.chmod(filename, mode)


def stop():
    # Save rules
    profile = config.get('PROFILE', '')
    if not len(profile):
        profile = 'iptables'

    profile_file = os.path.join('/var/lib/iptables', profile)
    profile_changes = '%s.saved' % profile_file

    base = {}
    changes = {}
    allowed_chains = {}

    for table in chains:
        allowed_chains[table] = config.get('SAVE_%s' % table.upper(), '').split()

    # Get base rules from /var/lib/iptables/<profile>
    if os.path.isfile(profile_file):
        rules = file(profile_file).read()
        base = parseConf(rules)

    changes = parseConf(getRules())

    # Save allowed changes to /var/lib/iptables/<profile>.saved
    diff = filterDict(diffDict(changes, base), allowed_chains)
    writeFile(profile_changes, makeConf(diff))

    # Clear chains & rules
    clear()

    # Remove lock file
    if os.access(lock_file, os.F_OK):
        os.unlink(lock_file)


def start():
    # Clear chains & rules
    clear()

    # Load rules
    profile = config.get('PROFILE', '')
    if not len(profile):
        profile = 'iptables'

    profile_file = os.path.join('/var/lib/iptables', profile)
    profile_changes = '%s.saved' % profile_file

    base = {}
    changes = {}
    allowed_chains = {}

    for table in chains:
        allowed_chains[table] = config.get('SAVE_%s' % table.upper(), '').split()

    # Load base rules
    if os.path.isfile(profile_file):
        rules = file(profile_file).read()
        base = parseConf(rules)
        restoreRules(rules)

    # Load allowed changes done in previous session
    if os.path.isfile(profile_changes):
        rules = file(profile_changes).read()
        changes = parseConf(rules)
        diff = filterDict(diffDict(changes, base), allowed_chains)
        restoreRules(makeConf(diff), flush=False)

    # Create lock file
    writeFile(lock_file, '')


def status():
    return os.access(lock_file, os.F_OK)
