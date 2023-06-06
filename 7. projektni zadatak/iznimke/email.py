class IznimkaEmail(Exception):
    def __init__(self):
        super(IznimkaEmail, self).__init__('Unesite ispravnu email adresu')
