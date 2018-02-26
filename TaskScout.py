#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Here we go. TaskScout V.3, Python Edition.

import argparse
import sys
output = "/home/geweih/output.txt"

# This is a function that opens up the output and reads it.
def fileread():
    f = open(output, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    return

parser = argparse.ArgumentParser(prog='TaskPy', description='TaskScout-Py. 100% betterer.')

# This is the main part of the script -- The 'addition' tag. Input here should be in quotes, double or otherwise.
parser.add_argument('-a', '--add', nargs='+',  default='',
        help="The task you're hoping to add.")

parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')

args=parser.parse_args()

#This prints the output to a file rather than to the terminal, allowing for recall of tasks later on after a break / program end.
print(args.add, file=open(output, "a"))

fileread()
