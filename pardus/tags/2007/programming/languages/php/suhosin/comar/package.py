config = '/etc/php/php.ini'
name = 'suhosin'

def postInstall():
    extension = 'extension=%s.so' % name
    lines = file(config).read().split('\n')
    if extension not in lines:
        lines.insert(1, extension)
        file(config, 'w').write('\n'.join(lines))

def preRemove():
    extension = 'extension=%s.so' % name
    lines = file(config).read().split('\n')
    if extension in lines:
        lines.remove(extension)
        file(config, 'w').write('\n'.join(lines))
