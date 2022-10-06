import csv
'''Open the file'''
f = open('flowers.csv')

'''Now read the fiel'''
#Note the csv.reader this is a requiredment
for row in csv.reader(f):
    print(row)
    # print(type(row))
f.close()