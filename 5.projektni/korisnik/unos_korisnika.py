from utilities import unos_pozitivnog_cijelog_broja
from .korisnik import Korisnik
def unos_korisnika(redni_broj):
    ime = input(f"Unesite ime {redni_broj}. korisnika: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").capitalize()
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")


    return Korisnik(ime, prezime, email, telefon)
