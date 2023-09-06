#!/usr/local/bin/python3
#/usr/bin/env python3
import os
import sys
import random

def check_reboot():
    return os.path.exists("run/reboot-required")

def new_function():
	return("Done")

def checkURLs():
	num = random.randint(1,2)
	if(num%2 == 0):
		return True
	else:
		return False


def main():
	new_function()
	if check_reboot():
		print("System Pending reboot.")
		sys.exit(1)
	else:
		print("all good.")
		exit(0)
	checkURLs()
main()
new_function()

