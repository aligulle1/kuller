import os
import os.path
import subprocess
import comar
import iptables


conf_file = '/etc/conf.d/iptables'


def runProc(cmd):
    return subprocess.call(cmd.split())


def setRule(rule):
    if getState() == 'off':
        fail('FW is offline')

    ret = runProc('/sbin/iptables %s' % rule)
    if ret != 0:
        fail('Invalid rule')


def loadConfig(conf):
    dict = {}
    try:
        for line in file(conf):
            if line != '' and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if value.startswith("'") or value.startswith('"'):
                    value = value[1:-1]
                dict[key] = value
    except:
        pass
    return dict


def setConfig(conf, new_values={}):
    new_conf = []
    updated = []

    for line in file(conf):
        if line != '' and not line.startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            if key not in new_values:
                new_conf.append(line)
                continue
            value = value.strip()
            if value.startswith("'") or value.startswith('"'):
                new_values[key] = '%s%s%s' % (value[0], new_values[key], value[0])
            new_conf.append('%s=%s\n' % (key, new_values[key]))
            updated.append(key)
        else:
            new_conf.append(line)

    for key in new_values:
        if key not in updated:
            new_conf.append('%s="%s"\n' % (key, new_values[key]))

    file(conf, 'w').write(''.join(new_conf))


def getServiceState(service):
    '''Get service state.'''
    link = comar.Link()
    link.call_package('System.Service.info', service)
    reply = link.read_cmd()
    return reply.command == 'result' and reply.data.split('\n')[1] in ['on', 'started']


def setServiceState(service, state):
    '''Set service state.'''
    link = comar.Link()
    link.call_package('System.Service.setState', service, {'state': state})
    link.read_cmd()

    if state == 'on':
        link.call_package('System.Service.start', service)
    else:
        link.call_package('System.Service.stop', service)
    link.read_cmd()


def getState():
    '''Get FW state'''
    config = loadConfig(conf_file)
    if getServiceState('iptables'):
        return 'on'
    return 'off'


def setState(state):
    '''Set FW state.'''
    if state not in ['on', 'off']:
        fail('Invalid state')
    if getState() == state:
        return

    if state == 'on':
        setServiceState('iptables', 'on')
    else:
        setServiceState('iptables', 'off')

    notify('Net.Filter.changed', 'state\n%s' % state)


def setProfile(profile, save_filter='', save_mangle='', save_nat='', save_raw=''):
    '''Set FW profile.'''
    state = getState()
    if state == 'on':
        setServiceState('iptables', 'off')

    conf = {
        'PROFILE': profile,
        'SAVE_FILTER': save_filter,
        'SAVE_MANGLE': save_mangle,
        'SAVE_NAT': save_nat,
        'SAVE_RAW': save_raw,
    }
    setConfig(conf_file, conf)

    if state == 'on':
        setServiceState('iptables', 'on')

    data = ['profile', profile, save_filter, save_mangle, save_nat, save_raw]
    notify('Net.Filter.changed', '\n'.join(data))


def getProfile():
    '''Get FW profile.'''
    config = loadConfig(conf_file)
    conf = [
        config.get('PROFILE', 'iptables'),
        config.get('SAVE_FILTER', ''),
        config.get('SAVE_MANGLE', ''),
        config.get('SAVE_NAT', ''),
        config.get('SAVE_RAW', ''),
    ]
    return '\n'.join(conf)


def getRules():
    '''Get user defined rules.'''
    if getState() == 'off':
        fail('FW is offline')

    config = loadConfig(conf_file)
    profile_file = os.path.join('/var/lib/iptables/', config.get('PROFILE', 'iptables'))

    base = {}
    changes = {}
    allowed_chains = {}

    for table in iptables.chains:
        allowed_chains[table] = config.get('SAVE_%s' % table.upper(), '').split()

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
            ret.append('%s %s' % (table, rule))
    return '\n'.join(ret)
