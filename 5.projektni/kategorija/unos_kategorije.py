from artikl import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja
from .kategorija import Kategorija

def unos_kategorije(redni_broj):
    naziv = input(f"Unesite naziv {redni_broj}. kategorije: ")

    broj_artikala = unos_pozitivnog_cijelog_broja(f"Unesite broj artikala za {redni_broj}. kategoriju: ")

    artikli = []
    for i in range(1, broj_artikala + 1):
        artikli.append(unos_artikla(i))

    artikl = artikli

    return Kategorija(naziv, artikl)