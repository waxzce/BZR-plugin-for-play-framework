#!/usr/bin/env python
# play build bzr plugin

"""A plugin to launch the play ant script after pull
"""

from bzrlib import branch
import os,os.path,subprocess

version_info = (0, 1, 0, 0)

def play_post_pull_hook(pull_result):
	if os.path.exists("framework/src/play"):
		print "Building Play! framework"
		savedPath = os.getcwd()
		os.chdir('framework')
		subprocess.Popen('ant').wait()
		os.chdir(savedPath)
		print "Done building Play! framework"

branch.Branch.hooks.install_named_hook('post_pull', play_post_pull_hook, 'Play! post_pull hook')

