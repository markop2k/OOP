def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()


def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. Email: {korisnik.email}, Telefon: {korisnik.telefon}"
