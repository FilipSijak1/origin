def unos_intervala(min, max):
    while True:
        try:
            broj = int(input('Odaberite redni broj stavke: '))

            if broj<min or broj>max:
                raise Exception('Unesli ste broj koji nije u intervalu.')

        except ValueError:
            print('Unesli ste slovo umjesto broja.')

        except Exception as e:
            print(e)

        else:
            return broj
