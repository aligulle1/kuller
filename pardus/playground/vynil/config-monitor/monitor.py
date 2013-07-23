#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

"""
config-monitoring

@author: Nicolas Lara
@license: GPL 2
@contact: nicolaslara@gmail.com
"""

import os
import time
from pyinotify import WatchManager, ThreadedNotifier, EventsCodes, ProcessEvent
import subversion
import settings

# TODO
# pyinotify does not follow symlinks
# manage symlinks

# Known Issues
# Problem adding directories recursivelly
# Fast add-remove relation

class EventProcessor(ProcessEvent):
    def process_IN_CREATE(self, event):
        if ('.svn' in event.name) or ('.svn' in event.path):
            return
        print 'Creating: %s' %  os.path.join(event.path, event.name)
        if event.is_dir:
            repo.mkdir(os.path.join(event.path, event.name))
        else:
            repo.add_commit(os.path.join(event.path, event.name))
        
    def process_IN_DELETE(self, event):
        if ('.svn' in event.name) or ('.svn' in event.path):
            return
        print 'Removing: %s' %  os.path.join(event.path, event.name)
        if event.is_dir:
            repo.del_commit(event.path)
        else:
            repo.del_commit(os.path.join(event.path, event.name))

    def process_IN_MODIFY(self, event):
        if ('.svn' in event.name) or ('.svn' in event.path):
            return
        print 'Modifing: %s' %  os.path.join(event.path, event.name)
        repo.mod_commit(os.path.join(event.path, event.name))

    def process_IN_MOVED_FROM(self, event):
        self.process_IN_DELETE(event)
        
    def process_IN_MOVED_TO(self, event):
        self.process_IN_CREATE(event)
        
    def process_IN_IGNORED(self, event):
        if settings.debug:
            print event
        else:
            pass

if __name__ == '__main__':
    mask = EventsCodes.IN_DELETE | EventsCodes.IN_CREATE | EventsCodes.IN_MODIFY | \
           EventsCodes.IN_MOVED_FROM | EventsCodes.IN_MOVED_TO
    repo = subversion.Manager(settings.repo_url)
    wm = WatchManager()

    notifier = ThreadedNotifier(wm, EventProcessor())
    notifier.start()

    wm.add_watch(settings.root, mask, rec=True, auto_add=True)
    wm.rm_watch(wm.get_wd(settings.root + ".svn"), rec=True)

    print 'start monitoring %s' % settings.root

    while True:
        try:
            time.sleep(0.01)
        except KeyboardInterrupt:
            # ...until c^c signal
            print 'stop monitoring...'
            notifier.stop()
            break
        except Exception, err:
            print err
