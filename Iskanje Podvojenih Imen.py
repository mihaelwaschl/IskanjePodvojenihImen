import csv

def read_file(csv_file):
    with open(csv_file, newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        word = []
        for row in file:
            word.append(row[0])
    return word

def get_duplicated_names():
    while True:
        try:
            data = read_file(input('Vnesi ime datoteke!\n'))
            count = 0
            for i in range(len(data)):
                if str(data[i]).upper() == str(data[i-1]).upper():
                    count += 1
                    print('Artikel {}, ki se nahaja na mestu {} je podvojen'.format(data[i], i+1))
            if count == 0:
                print('V datoteki ni podvojenih artiklov.')
            break

        except FileNotFoundError:
            print('Datoteka ne obstaja ali ni v isti mapi, kot program! Poiskusi ponovno.')

get_duplicated_names()
