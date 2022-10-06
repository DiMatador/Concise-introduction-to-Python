import sys

infile = sys.argv[1]
outfile = sys.argv[2]
# outfile1 = sys.argv[3]

infile = open(infile)
outfile = open(outfile, 'w')
# outfile1 = open(outfile1, 'w')

for line in infile:
    outfile.write(line)
    line = line.strip('\n')
    line = str(len(line))
    # outfile.write(line + '\n')

infile.close()
outfile.close()
# outfile1.close()