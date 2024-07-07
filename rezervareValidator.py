from Domain.rezervare import Rezervare


class RezervareValidator:
    def valideaza(self, rezervare: Rezervare):
        erori = []
        if rezervare.nume == '':
            erori.append("Numele nu poate fi un string gol")
        if len(erori) > 0:
            raise ValueError(erori)
