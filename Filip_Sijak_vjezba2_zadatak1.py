kolegij = {}

naziv_kolegija = input('\nUnesite ime kolegija: ')
naziv_kolegija = naziv_kolegija.upper()
ETCS_bodovi = int(input('Unesite ECTS bodove za kolegij: '))
kolegij['kolegij'] = ETCS_bodovi, naziv_kolegija

print('Kolegij', naziv_kolegija, 'nosi', ETCS_bodovi, 'ECTS bodova', end='.')
