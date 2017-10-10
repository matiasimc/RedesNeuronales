import csv
import sys

def unicode_csv_reader(utf8_data, **kwargs):
    csv_reader = csv.reader(utf8_data, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def parse_csv(filename):
    poemas = []
    with open(filename, 'rb') as csvfile:
        reader = unicode_csv_reader(csvfile, delimiter='#')
        for row in reader:
            for poema in row:
                estrofas = []
                reader2 = unicode_csv_reader([poema.encode('utf-8')], delimiter='%')
                for row2 in reader2:
                    for estrofa in row2:
                        reader3 = unicode_csv_reader([estrofa.encode('utf-8')], delimiter='&')
                        for row3 in reader3:
                            estrofas.append(row3)
                poemas.append(estrofas)
    return poemas


def print_poema(num):
    poema =  parse_csv("data/neruda.csv")[num]
    for estrofa in poema:
        for verso in estrofa:
            print verso
        print ""
