import sys

def problem3_6(infilename, outfilename):
    charct = 0

    infile = open(infilename)
    outfile = open(outfilename, 'w')
    outfile.write(infile)
    
    # for line in infile:
    #     print(line, end='')
        # l = line.strip()
        # charct =  len(l)       
        
        # print(charct)

    infile.close()
    outfile.close()

problem3_6('HumptyDumpty.txt', "newHumpty.txt")