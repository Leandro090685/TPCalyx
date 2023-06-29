import csv
f= open("conjunto_A.csv")
reader = csv.reader(f)
for row in reader:
    print (row) 