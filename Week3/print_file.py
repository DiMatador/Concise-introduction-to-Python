# - print_file.py *- coding: utf-8 -*-
""" Opens file and prints its contents line by line. """

import sys     # we need this library to deal with operating system

filename = sys.argv[1]

infile = open(filename)

for line in infile:
    print(line,end="") # the file has "\n" at the end of each line already

infile.close()

#%%

import sys

filename = sys.argv[1]

infile = open(filename)


def problem3_1(infile):
    charcount = 0
    charcount += 1
    return len(open(charcount).read())

    problem3_1(infile)

print(problem3_1(infile))
infile.close()
