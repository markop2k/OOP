class Kategorija:
    def __init__(self, naziv, artikl):
        self.__naziv = naziv
        self.__artikl = artikl

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv= naziv

    @property
    def artikl(self):
        return self.__artikl

    @artikl.setter
    def artikl(self, artikl):
        self.__artikl = artikl

    def ispis(self):
        print(f'{self.naziv}')