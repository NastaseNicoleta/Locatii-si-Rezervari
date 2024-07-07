from Domain.locatie import Locatie


class LocatieValidator:
    def valideaza(self, locatie: Locatie):
        erori = []
        if locatie.nume == '':
            erori.append("Numele nu poate fi gol!")
        if locatie.capacitate <= 0:
            erori.append("Capacitatea trb sa fie pozitiva")
        if int(locatie.capacitate) != locatie.capacitate:
            erori.append("Locatia trb sa fie nr intreg!")
        if len(erori) > 0:
            raise ValueError(erori)
