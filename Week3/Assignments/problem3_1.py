def problem3_1(txtfilename):
    f = open(txtfilename)
    characters = 0
    for lin in f:
        print(lin, end='')
        characters = characters + len(lin)
    print('\n\nThere are',characters,'letters in the file')
    f.close()

