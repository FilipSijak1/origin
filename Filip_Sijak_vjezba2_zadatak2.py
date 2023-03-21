import datetime

kolegij = {}
kolegij['ime'] = input('\nUnesite ime kolegija: ').upper()
kolegij['ECTS'] = int(input('Unesite ECTS bodove za kolegij: '))

dan = int(input('Unesite dan ispita: '))
mjesec = int(input('Unesite mjesec ispita: '))
godina = int(input('Unesite godinu ispita: '))

date = datetime.date(godina, mjesec, dan)

ispit = {}
ispit['datum'] = date
ispit['kolegij'] = kolegij

print('Kolegij', ispit['kolegij']['ime'], 'nosi', ispit['kolegij']['ECTS'], 'ECTS bodova', end='.')
print(' Datum ispita je:', date, end='.')

