import csv

def read_file(csv_file):
    with open(csv_file, newline='', encoding= 'utf8' ) as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        #
        # for row in file:
        #     print(row)
    return file

def proces_one_line():
    while True:
        try:
            data = read_file(input('Vnesi ime datoteke!\n'))
            break
        except FileNotFoundError:
            print('Datoteka ne obstaja ali ni v isti mapi, kot program! Poizkusi ponovno.')
    print(data)

proces_one_line()
