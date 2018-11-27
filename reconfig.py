#!/bin/env python3

import os
import re
import subprocess
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

home = os.environ['HOME']
videoRaw = subprocess.run(['xrandr'], stdout=subprocess.PIPE).stdout.decode('utf-8')
monitors = []
# DP-0 connected primary 2560x1440+0+0
found = re.findall(r'(.*?) connected .*?\d+x\d+\+(\d+)\+(\d+)',videoRaw)
for x in found:
	if x[1]=='0' and x[2]=='0':
		monitors.append(x[0])
for x in found:
	if x[1]!='0' or x[2]!='0':
		monitors.append(x[0])

i3Config = env.get_template('config.j2')
with open("config", "w") as cfg:
	cfg.write(i3Config.render(
		monitors=monitors, 
		twomonitors=len(monitors)==2,
		home=home,
	))


blockConfig = env.get_template('i3blocks.j2')
with open("blocks.conf", "w") as cfg:
	cfg.write(blockConfig.render(home=home))