from Utilities import unos_intervala
from kolegij import unos_kolegija, ispis_svih_kolegija

kolegiji = []

running = True
while running:
    print('-'*20)
    print('1. Unos novog kolegija')
    print('2. Unos novog ispita')
    print('3. Unos novog studenta')
    print('4. Ispis kolegija')
    print('5. Ispis ispita')
    print('6. Ispis studenata')
    print('7. Zaustavi program')
    print('-' * 20)

    akcija = unos_intervala(1, 7)

    if akcija == 1:
        kolegiji.append(unos_kolegija(len(kolegiji)+1))

    elif akcija == 4:
        ispis_svih_kolegija(kolegiji)


    if akcija == 7:
        running = False

