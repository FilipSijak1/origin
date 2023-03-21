kolegij = {}
kolegij['ime'] = input('\nUnesite ime kolegija: ').upper()
kolegij['ECTS'] = int(input('Unesite ECTS bodove za kolegij: '))

print('Kolegij', kolegij['ime'], 'nosi', kolegij['ECTS'], 'ECTS bodova', end='.')
