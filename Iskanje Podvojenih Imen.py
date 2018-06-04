import csv

def read_file(csv_file):
    with open(csv_file, newline='', encoding= 'utf8' ) as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        word = []
        for row in file:
            word.append(row[0])
    return word

def get_duplicated_names():
    while True:
        try:
            data = read_file(input('Vnesi ime datoteke!\n'))
            for i in range(len(data)):
                if data[i] == data[i-1]:
                    print('Artikel {}, ki se nahaja na mestu {} je podvojen'.format(data[i], i+1) )
            break
        except FileNotFoundError:
            print('Datoteka ne obstaja ali ni v isti mapi, kot program! Poizkusi ponovno.')

get_duplicated_names()