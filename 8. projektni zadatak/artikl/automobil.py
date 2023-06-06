from .vozilo import Vozilo
from .artikl import Artikl

class Automobil(Artikl,Vozilo):

    def __init__(self, naslov, opis, cijena, snaga):
        super().__init__(naslov, opis, cijena)
        self.snaga = snaga

    def ispis(self):
        return f'{self.naslov}, {self.opis}, {self.cijena}, {self.snaga}'
        #print('Informacije o vozilu: ')
        #print(f'\t Naslov: {self.naslov}')
        #print(f'\t Opis: {self.opis}')
        #print(f'\t Cijena: {self.cijena}')
        #print(f'\t Cijena osiguranja: {self.cijena_osiguranja(self.snaga)}')
        