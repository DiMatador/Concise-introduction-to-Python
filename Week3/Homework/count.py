"""
lwc.py below is a program that counts the number of lines, words, and
characters in a text file.  Similar to linux wc command.
Copy this to a separate file named lwc.py or download ours.
"""
import sys

# filename = sys.argv[1]
filename = input('Enter a file name: ')
infile = open(filename)

#initialize line, word, and char counter to 0
linect = 0
wordct = 0
charct = 0

for line in infile:
    linect = linect + 1  # the
    for word in line.split():
        wordct = wordct + 1
    charct = charct + len(line)

infile.close()

print('Lines in file:',linect,',','Words in file:',wordct,',','Characters in file:', charct)
