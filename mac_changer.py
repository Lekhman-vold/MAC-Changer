#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:12:13:14:15", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
subprocess.call("ifconfig")