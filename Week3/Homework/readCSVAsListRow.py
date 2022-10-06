import csv

f = open('flowers.csv')
'''Create an empty list to add the csv to it '''
data = []
'''Read a file into a list '''
for row in csv.reader(f):
#'''append the csv to the empty list data'''
    data.append(row)
print(data)#print the data list with csv in it

f.close()#close the file
