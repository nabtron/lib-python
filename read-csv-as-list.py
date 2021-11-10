import csv

with open('trade_data_for_nabtron.csv') as csv_file:
    csv_list = list(csv.reader(csv_file, delimiter=","))
    line_count = 0
    for row in csv_list:
        if(line_count == 0):
            line_count += 1
        else:
            print(row[10])
