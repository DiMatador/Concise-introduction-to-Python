#print_file.py *_coding: utf-8 -*-
"""Opens file and prints its contentes line by line. """

import sys # we need to import this library to deal with operating system

filename = sys.argv[1] #use one argument cuss its only one file to specify in the cmd

infile = open(filename)

for line in infile:
    print(line, end='') # The file has "\n" at the end of each line already, we use "end=''" to remove that line

infile.close()
