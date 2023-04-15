def ispis_ispita(ispit):
    print(f"\tIspit iz kolegija {ispit['kolegij']['ime']}, koji nosi {ispit['kolegij']['ects']}"
          f" ECTS-a i koji će se održati {ispit['datum']}.")

def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. Ispit iz kolegija {ispit['kolegij']['ime']}"

def ispis_svih_ispita(ispiti):
    print('Popis svih ispita: ')
    for ispiti in ispiti:
        ispis_ispita(ispiti)