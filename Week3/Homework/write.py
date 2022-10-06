import sys

filename = sys.argv[1]
outfile = open(filename)

def write_toFile(filename,name,age,major):
    outfile = open(newFile.txt, 'w')
    name = "Julio Davila"
    age = 48
    major = 'Python Data Scient'
    major = "Python Data Scientist"
    outfile = write("My name is "+name)
    outfile = write("My age is "+srt(age))
    outfile = write("and I major in" + major)

    outfile.close()
# def write_to_file(filename, myname, myage, major):
#     # open file first
#     outfile = open(filename,'w')
#     outfile.write("My name is "+ myname + " \n")
#     outfile.write("My age is " + myage + "\n")
#     outfile.write("I am majoring in " + major + "\n")
#     # write out the age and major in two lines
#     # close the file
#     outfile.close()
