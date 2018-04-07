import csv #import csv library
import re
f = open('/home/rashad/data/66-1/0-1000_argus_flow.txt') #open csv file and 
csv_f = csv.reader(f) #reads file
#search0obj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
for row in csv_f:
    if re.match('State', row):
        break
    else:
        print row[8]
f.close()

file1 = open(/home/rashad/data/66-1/0-1000_argus_flow.txt, 'rb')
reader = csv.reader(file1)
new_rows_list = []
for row in reader:
    
   if row[2] == 'Test':
      new_row = [row[0], row[1], 'Somevalue']
      new_rows_list.append(new_row)
file1.close()   # <---IMPORTANT

# Do the writing
file2 = open(file.csv, 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()
