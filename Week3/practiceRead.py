import sys

filename = sys.argv[1]

infile = open(filename)

for each in infile:
    print(each, end='')

infile.close()
