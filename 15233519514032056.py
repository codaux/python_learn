import hashlib
import csv

# make a rainbow dictionary of all possible passwords hash.
dict = {}
for num in range(0,9999):
    dict[hashlib.sha256('%04d' % num).hexdigest()]  = '%04d' % num
with open('1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print ('%10s password is %s' % (str(row[0]), str(dict[row[1]])))