import csv
import sys
import random

if len(sys.argv) < 2:
    raise Exception("lista nu a fost specificata")

lista_studenti = sys.argv[1]

studenti = []

with open(lista_studenti, "r") as f:
    data = csv.reader(f)
    next(data, None)
    for row in data:
        # print(row)
        studenti.append(row[0])


studenti_alesi = random.sample(studenti, 3)

print("Studentii alesi sunt: ")
print(studenti_alesi)