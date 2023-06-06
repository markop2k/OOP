from datetime import date
from iznimke import IznimkaTelefon, IznimkaPrazanTekst, IznimkaEmail, IznimkaTekst


def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati cijeli pozitivni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati pozitivni realni broj!')

        except ValueError:
            print('Unijeli ste znak, a ne realni broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):
    while True:
        try:
            dan = int(input(poruka))
            mjesec = int(input(f'Unesite mjesec isteka prodaje: '))
            godina = int(input(f'Unesite godinu isteka prodaje: '))
            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        else:
            return datum


def unos_teksta(poruka):
    while True:
        try:
            tekst = input(poruka)

            if not tekst.isalpha():
                raise Exception("Morate unijeti samo slova!")

        except Exception as e:
            print(e)

        else:
            return tekst


def unos_emaila(poruka):
    while True:
        email = input(poruka)

        try:
            email.index("@")

        except ValueError:
            print("Morate unijeti ispravnu email adresu!")

        else:
            return email


def unos_telefona(poruka):
    while True:
        try:
            broj = unos_pozitivnog_cijelog_broja(poruka)

            broj_znamenki = str(broj)

            if len(broj_znamenki) > 12:
                raise Exception('Broj mora imati do 12 znamenki!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Morate upisati broj u intervalu {min}-{max}!")

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def provjera_korisnickog_unosa_privatni(telefon, email, ime, prezime):
    while True:
        try:
            if len(telefon) == 0 or len(email) == 0 or len(ime) == 0 or len(prezime) == 0:
                raise IznimkaPrazanTekst()
            elif len(str(telefon)) != 8:
                raise IznimkaTelefon()
            elif "@" not in email:
                raise IznimkaEmail()
            elif not ime.isalpha() & prezime.isalpha():
                raise IznimkaTekst()

            int(telefon)

        except IznimkaPrazanTekst as e:
            return str(e)

        except IznimkaTelefon as f:
            return str(f)

        except IznimkaEmail as g:
            return str(g)

        except IznimkaTekst as h:
            return str(h)

        except ValueError:
            return ('Telefon mora biti broj')

        else:
            return None


def provjera_korisnickog_unosa_poslovni(telefon, email, naziv, web):
    while True:
        try:
             if len(telefon) == 0 or len(email) == 0 or len(naziv) == 0 or len(web) == 0:
                 raise IznimkaPrazanTekst()
             elif len(str(telefon)) != 8:
                 raise IznimkaTelefon()
             elif "@" not in email:
                raise IznimkaEmail()

             int(telefon)

        except IznimkaPrazanTekst as e:
            return str(e)

        except IznimkaTelefon as f:
            return str(f)

        except IznimkaEmail as g:
            return str(g)

        except ValueError:
            return ('Telefon mora biti broj')

        else:
            return None


def provjera_unosa_artikla(naslov, opis, cijena, snaga):
    try:
        if len(naslov) == 0 or len(opis) == 0 or cijena == '' or snaga == '':
            raise IznimkaPrazanTekst()

        if int(cijena) < 0 or int(snaga) < 0:
            raise Exception(f"Potrebno upisati pozitivan cijeli broj!")

    except IznimkaPrazanTekst as e:
        return str(e)

    except ValueError:
        return('Potrebno upisati broj!')

    except Exception as e:
        return str(e)


def provjera_unosa_prodaje(korisnik, prodaja):
    try:
        if korisnik == '' or prodaja == '':
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)
