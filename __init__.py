#!/usr/bin/env python
# play build bzr plugin

"""A plugin to launch the play ant script after pull
"""

from bzrlib import branch
import os,os.path

version_info = (0, 2, 0, 0)

def play_post_pull_hook(pull_result):
	if os.path.exists("framework/src/play"):
		savedPath = os.getcwd()
		os.chdir('framework')
		print "Building Play! framework"
		os.execl('/usr/bin/ant')
		print "Done building Play! framework"
		os.chdir(savedPath)

branch.Branch.hooks.install_named_hook('post_pull', play_post_pull_hook, 'Play! post_pull hook')

