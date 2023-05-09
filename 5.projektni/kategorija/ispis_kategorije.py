from artikl import ispis_artikla

def get_kategorija(redni_broj, kategorija):
    return f'\t{redni_broj}. {kategorija.naziv}'


def ispis_svih_kategorija(kategorije):
    for kategorija in kategorije:
        kategorija.ispis()

        for j, artikl in enumerate(kategorija.artikl, start=1):
            print(f"Informacije o {j}. artiklu: ")
            artikl.ispis()

        print("\n")
