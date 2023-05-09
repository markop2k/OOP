class Prodaja:
    def __init__(self, datum, korisnik, artikl):
        self.datum = datum
        self.korisnik = korisnik
        self.artikl = artikl

    def ispis(self):
        print('Informacije o korisniku: ')
        self.korisnik.ispis()

        print('Informacije o artiklu: ')
        self.artikl.ispis()

        print('Datum isteka prodaje: ')
        print(f'\t Dan: {self.datum.day}')
        print(f'\t Mjesec: {self.datum.month}')
        print(f'\t Godina: {self.datum.year}')

        print("\n")
