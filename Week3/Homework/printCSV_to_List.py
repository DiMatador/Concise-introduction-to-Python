import csv

f = open('BooksRead.csv')

for row in csv.reader(f):
    '''Write rows into lists like so'''
    print(row[0], row[1], row[2])

f.close()