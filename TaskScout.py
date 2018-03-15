#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TaskScout 3 - Cross the water -- Home through the town, past the shadows.

import argparse
import sys
import os

output = "/home/geweih/output.txt"

# This is a function that opens up the output and reads it. // Fall down wherever we meet...
def fileread():
    f = open(output, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    return

# Clearsave function.
def RememberAnna():
    ## You're going to want to save the file in a directory here.
    ## List the directory as a var for the sake of ease.
    os.remove(output)
    print("Anna begins to change her mind. // List sent to the Boatman.")
    return

# Clear function.
def ForgetItAll():
    os.remove("/home/geweih/output.txt")
    print("All your love was just a dream. // Just like that, it's over.")
    return

parser = argparse.ArgumentParser(prog='TaskPy', description='TaskScout-Py. 100% betterer.')
# This is the main part of the script -- The 'addition' tag. Input here should be in quotes, double or otherwise. // I'm almost drowning in her sea.
parser.add_argument('-a', '--add', nargs='+', default='-',
        help="The task you're adding. All input will be accepted as one line. If you want different tasks on different lines, please add them one-by-one.")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0');
parser.add_argument('-c' ,dest="clear", action='store_const'  ,const=True)
parser.add_argument('-cs',dest="clearsave", action='store_const',const=True)

results = args=parser.parse_args()

#This prints the output to a file rather than to the terminal, allowing for recall of tasks later on after a break / program end. // Take the way home.
print(args.add, file=open(output, "a"))

if results.clear:
    ForgetItAll()
else:
    if results.clearsave:
        RememberAnna()
    else:
        fileread()
