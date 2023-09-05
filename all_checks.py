#!/usr/local/bin/python3
#/usr/bin/env python3
import os
import sys

def check_reboot():
    return os.path.exists("run/reboot-required")

def main():
    if check_reboot():
        print("Pendig reboot.")
        sys.exit(1)
    else:
        print("all good.")
        exit(0)
main()

