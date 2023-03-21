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

student = {}
student['ime'] = input('Unesite ime studenta: ').title()
student['prezime'] = input('Unesite prezime studenta: ').title()
student['ispit'] = ispit

print('Student', student['ime'], student['prezime'], 'je prijavio ispit iz kolegija',
      student['ispit']['kolegij']['ime'], 'koji će se održati',  student['ispit']['datum'], end='.')
