#!/usr/local/bin/python3
#/usr/bin/env python3
import os
import sys

def check_reboot():
    return os.path.exists("run/reboot-required")

def new_function():
	return("Done")


def main():
	new_function()
	if check_reboot():
		print("System Pending reboot.")
		sys.exit(1)
	else:
		print("all good.")
		exit(0)
main()
new_function()

