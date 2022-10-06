'''this is not working yet'''

import sys

filename = sys.argv[1]
outfile = sys.argv[2]
infile = open(filename)
outfile = open(filename, 'w')

def problem3_6(infile):
    ct = 0

    for line in infile:
        outfile.write(line)
        print(line, end='')

    for line in outfile:
        for word in line.lower().split():
            word = word.strip("'?,.;!-/\"")
        ct = ct + 1



filename.close()
outfile.close()