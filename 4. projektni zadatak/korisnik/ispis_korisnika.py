def ispis_korisnika(korisnik):
   print(f"Informacije o korisniku: ",
    f"\n\tIme: {korisnik['ime']}",
    f"\n\tPrezime: {korisnik['prezime']}",
    f"\n\tTelefon: {korisnik['telefon']}",
    f"\n\tEmail: {korisnik['email']}")


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        ispis_korisnika(korisnik)


def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"
