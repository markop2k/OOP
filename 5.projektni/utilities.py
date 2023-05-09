from datetime import date

def unos_pozitivnog_cijelog_broja(poruka):

    while True:
        try:
            broj = int(input(f"{poruka}"))

            if broj < 0:
                raise Exception(f"Upisana vrojednost nije pozitivan cijeli broj!")

        except ValueError:
            print('Morate upisati cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):

    while True:
        try:
            broj = float(input(f"{poruka}"))

            if broj < 0:
                raise Exception(f"Upisana vrojednost nije pozitivan realni broj!")

        except ValueError:
            print('Morate upisati realan broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):

    while True:
        try:
            dan = int(input(f"Unesite dan isteka prodaje: "))
            mjesec = int(input(f"Unesite mjesec isteka prodaje: "))
            godina = int(input(f"Unesite godinu isteka prodaje: "))

            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        else:
            return datum


def unos_intervala(min,max):

    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Broj nije u intervalu od {min} do {max}")

        except ValueError:
            print('Morate upisati broj!')

        except Exception as e:
            print(e)

        else:
            return broj


