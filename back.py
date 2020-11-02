import csv

with open('problems.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Kolumny to {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t dla pytania {row[0]} odzpowiedzia jest {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

odpowiedz = '7'
line_count = 1
if line_count == 1 and row[1] == odpowiedz:
    print('True')
