from .artikl import Artikl

class Stan(Artikl):

    def __init__(self, naslov, opis, cijena, kvadratura):
        super().__init__(naslov, opis, cijena)
        self.kvadratura = kvadratura

    def ispis(self):
        return f'{self.naslov}, {self.opis}, {self.cijena}, {self.kvadratura}'
        #print('Informacije o stanu: ')
        #print(f'\t Naslov: {self.naslov}')
        #print(f'\t Opis: {self.opis}')
        #print(f'\t Cijena: {self.cijena}')
        #print(f'\t Kvadratura: {self.kvadratura}')