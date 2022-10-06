import sys
infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename, 'w')

for eachL in infile:
	outfile.write(eachL)

infile.close()
outfile.close()
