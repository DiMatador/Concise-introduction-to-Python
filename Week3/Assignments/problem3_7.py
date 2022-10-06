import csv

def problem3_7(csv_pricefile, flower):
    f = open(csv_pricefile)
    reader = csv.reader(f)
    for row in reader:
        if row[0] == flower:
            print(row[1])

