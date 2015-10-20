# Turn on/off touchpad.

# Turn touchpad off:
# xinput list | python get-touchpad-id.py 0

# Turn touchpad on:
# xinput list | python get-touchpad-id.py 1

# On Ubuntu, this command line:
#  xinput set-prop nn "Device Enabled" m
#
# toggles the status of a device where nn identifies
# the device id and m is either 1 (enabled) or 0 (disabled).
#
# The command line
#   xinput list
# emits the list of devices and their ids.
#
# The output of 'xinput list' is piped into this Python
# script to determine the Synaptics TouchPad id. That value
# is reported in a line formatted like this:
#
# SynPS/2 Synaptics TouchPad                id=18   [slave  pointer  (2)]
#
# First, a regex search is performed to identify the line above and then
# another regex search is performed to extract the device id. Python's
# templating is used to create the command line needed to toggle the
# touchpad status.

# That command is call with Python's os.system() method.

import re
import string
import os
import sys

touchpadStatus = str(sys.argv[1])

data = sys.stdin.readlines()
for line in data:
    if re.search('Synaptics TouchPad', line):
        match = re.search('id=(\d{1,2})', line)
        if match:
            tmpl = string.Template("xinput set-prop $id \"Device Enabled\" $touchpadStatus")
            cmd = tmpl.substitute(id=match.group(1), touchpadStatus=touchpadStatus)

            os.system(cmd)

            if touchpadStatus == '1':
                print 'Touchpad enabled'
            else:
                print 'Touchpad disabled'

            break