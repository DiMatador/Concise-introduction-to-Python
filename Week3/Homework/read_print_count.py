""" Function that reads text file and counts the number of characters in the file.
    Print both the text file and the number of characters. make sure is not doubled space also
    skip a line before printing the count. """

import sys

filename = sys.argv[1]

infile = open(filename, 'r')

def charcount(infile):
    return len(open(infile).read())
charcount(infile)

print(charcount(infile))
infile.close()
