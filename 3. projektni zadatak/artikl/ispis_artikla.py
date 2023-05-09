def ispis_artikla(artikl):
    print(f"Informacije o artiklu: ",
          f"\n\tnaslov: {artikl['naslov']}",
          f"\n\topis: {artikl['opis']}",
          f"\n\tcijena: {artikl['cijena']}")

def get_artikl(redni_broj, artikl):
    return f"{redni_broj}. {artikl['naslov']} "