import csv
import time

with open('problems.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    poprawne = 0
    wszystkie = 0
    for row in csv_reader:
        print(row[0])
        odpowiedz = input("odpowiedz:\n")
        if odpowiedz == row[1]:
            print('True')
            line_count += 1
            poprawne += 1
        else:
            print('False')
            line_count += 1
wszystkie = line_count
print(poprawne,'/',wszystkie)