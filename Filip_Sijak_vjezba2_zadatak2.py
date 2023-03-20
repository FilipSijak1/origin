import datetime

kolegij = {}
naziv_kolegija = input('\nUnesite ime kolegija: ')
naziv_kolegija = naziv_kolegija.upper()
ETCS_bodovi = int(input('Unesite ECTS bodove za kolegij: '))
kolegij['Parametri kolegija'] = ETCS_bodovi, naziv_kolegija

ispit = {}
dan_ispita = int(input('Unesite dan ispita: '))
mjesec_ispita = int(input('Unesite mjesec ispita: '))
godina_ispita = int(input('Unesite godinu ispita: '))
ispit['Datum ispita'] = godina_ispita, mjesec_ispita, dan_ispita
ispit.update(kolegij)
# ispit_update = ispit | kolegij
date = datetime.date(godina_ispita, mjesec_ispita, dan_ispita)

print('Kolegij', naziv_kolegija, 'nosi', ETCS_bodovi, 'ECTS bodova', end='.')
print(' Datum ispita je:', date, end='.')
