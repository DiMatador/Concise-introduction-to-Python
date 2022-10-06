import sys

filename = sys.argv[1]
infile = open(filename)

#read each line
for eachL in infile:
	print(eachL, end='')
infile.close()
