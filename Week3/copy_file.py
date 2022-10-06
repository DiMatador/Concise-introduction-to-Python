
import sys
infilename = sys.argv[1]
outfilename = sys.argv[2]

""" Opens two files and copies one into the other line by line. """
infile = open(infilename)
outfile = open(outfilename,'w')

for line in infile:
    outfile.write(line)

infile.close()
outfile.close()
