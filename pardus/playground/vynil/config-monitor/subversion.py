#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import pysvn
import settings
import re
from copy import copy

class Manager:
    """
    Wrapper for pysvn methods
    """

    def __init__(self, repo_url):
        self.client = pysvn.Client(repo_url)
        self.re = re.compile('^\-\-\*\*\-\-(?P<comment>.*)\-\-\*\*\-\-', re.S)
        

    def notify(self, msg):
        print msg

    def get_msg(self, path, action, dir=False):
        if dir:
            return "No message was specified\n Action: %s\n File: %s\n"\
                   % (action, path)
        f = open(path, 'r')
        txt = f.read()
        f.close()
        match = self.re.match(txt) 
        if match:
            f = open(path, 'w')
            f.write(self.re.sub('', txt))
            f.close()
            return match.groupdict()['comment']
        else:
            return "No message was specified\n Action: %s\n File: %s\n"\
                   % (action, path)
        
    def commit(self, path, msg):
        self.client.checkin(path, msg)
        
    def add_commit(self, path, dir=False):
        """
        Commits a new file to the repository
        """
        try:
            msg = self.get_msg(path, 'add_commit', dir)
            self.client.add(path, recurse=dir)
            self.commit(path, msg)
            self.notify('Added file %s to the repository\n' % path)
        except IOError:
            self.notify('File %s does not exist anymore or is already under'+\
                        ' version control. Not adding\n' % path)
            
    def mod_commit(self, path):
        """
        Commits a file that has been modified to the repository
        """
        try:
            msg = self.get_msg(path, 'mod_commit')
            self.commit(path, msg)
            self.notify('Modified file %s in the repository\n' % path)
        except IOError:
            self.notify('File %s does not exist anymore. Not adding\n' % path)

    def del_commit(self, path):
        """
        Commits the deletion of a file to the repository
        """
        #         try:
        #             self.client.remove(path, force=True)
        #             self.notify('Deleted file %s in the repository\n' % path)
        #         except pysvn.ClientError:
        #             self.notify('Various files deleted for %s\n' % settings.root)
        
        try:
            self.client.remove(path, force=True)
            self.commit(path, 'Deleted file %s' % path)
            self.notify('Deleted file %s in the repository\n' % path)
        except pysvn.ClientError:
            changes, old_changes = [0],[0,0]
            while(len(changes) != len(old_changes)):
                old_changes = copy(changes)
                changes = self.client.status(settings.root)
                for mf in changes:
                    if mf.text_status == pysvn.wc_status_kind.missing:
                        self.client.remove(mf.path, force=True)
            
            self.commit(settings.root,\
                        'Various files have been deleted. Force deleting %s'\
                        % path) 
            self.notify('Various files deleted for %s. Force deleting %s\n'\
                        % (path, path))
        

    def mkdir(self, path):
        """
        Creates a new directory in the repository
        """
        self.client.add(path, recurse=False)
        self.commit(path, 'Created directory %s' % path)
        self.notify("Created directory %s\n" % path)
                
