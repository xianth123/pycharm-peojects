import csv

csv_file = open('csv.csv','w+')
try:
    writer = csv.writer(csv_file)
    writer.writerow(('number', 'number pius 2', 'number times 3'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csv_file.close()