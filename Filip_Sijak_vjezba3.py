from datetime import date
kolegiji = []
ispiti = []
studenti = []

broj_kolegija = int(input('Unesite broj kolegija: '))

for i in range(1, broj_kolegija+1):
    kolegij = {}
    kolegij["ime"] = input(f'Unesite ime {i}. kolegija: ')
    kolegij["ects"] = int(input(f'Unesite ECTS bodove {i}. kolegija: '))
    kolegiji.append(kolegij)

broj_ispita = int(input('Unesite broj ispita: '))

for i in range(1, broj_ispita+1):
    ispit = {}
    print('Popis svih kolegija: ')
    for j, kolegij in enumerate(kolegiji, start=1):
        print(f'\t{j}. {kolegij["ime"]}')

    odabrani_kolegij = int(input('Odaberite kolegij: '))
    dan = int(input('Unesite dan ispita: '))
    mjesec = int(input('Unesite mjesec ispita: '))
    godina = int(input('Unesite godinu ispita: '))
    ispit["datum"] = date(godina, mjesec, dan)
    ispit["kolegij"] = kolegiji[odabrani_kolegij-1]
    ispiti.append(ispit)

broj_studenata = int(input('Unesite broj studenata: '))

for i in range(1, broj_studenata+1):
    student = {}
    student["ime"] = input(f'Unesite ime {i}. studenta: ')
    student["prezime"] = input(f'Unesite prezime {i}. studenta: ')
    for j, ispit in enumerate(ispiti, start=1):
        print(f'\t{j}. ispit iz kolegija {ispit["kolegij"]["ime"]}')

    odabrani_ispit = int(input('Odaberite ispit: '))
    student["ispit"] = ispiti[odabrani_ispit-1]
    studenti.append(student)

print('Popis svih studenata: ')
for student in studenti:
    print(f'\t Student {student["ime"]} {student["prezime"]} je prijavio:')
    print(f'\t\tispit iz kolegija {student["ispit"]["kolegij"]["ime"]} koji će se održati {student["ispit"]["datum"]}')
