# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here

filename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(filename)
outfile = open(outfilename, 'w')

ct = 0

for line in infile:
    outfile.write(line)
    print(line, end='')

for line in outfile:
    for word in line.lower().split():
        word = word.strip("'?,.;!-/\"")
    ct = ct + 1

print(line, end='')
print(ct)