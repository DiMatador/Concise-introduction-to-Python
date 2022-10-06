def problem3_1(txtfilename) :
    f = open(txtfilename)
    characters = 0
    for lin in f :
        print(lin, end='')
        characters = characters + len(lin)
    print('\n\nThere are',characters,'letters in the file')
    f.close()

problem3_1('HumptyDumpty.txt')




humpty = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.'''

# def problem3_1(textfilename) :
#     characters = 0
#     for lin in humpty :
#         print(lin, end='')
#         characters = characters + len(lin)
#     print('\nThere are',characters,'letters in the file')
    
# problem3_1('HumptyDumpty.txt')





