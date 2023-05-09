def get_korisnik(redni_broj, korisnik):
    return f'\t{redni_broj}. {korisnik.ime} {korisnik.prezime}'


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        print("Informacije o korisniku: ")
        korisnik.ispis()