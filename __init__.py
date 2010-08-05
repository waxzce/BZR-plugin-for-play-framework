## play build bzr plugin

"""A plugin for launch the play ant script after pull
"""
import subprocess
import os.path

from bzrlib import branch

version_info = (0, 1, 0, 'dev', 0)

def play_post_pull_hook(pull_result):
	if os.path.exists("framework/src/play"):
		print "launch the play ant script"
		#LAUNCH ANT HERE

branch.Branch.hooks.install_named_hook('post_pull', play_post_pull_hook, 'play post_pull hook')

