import jsonpickle

from Domain.rezervare import Rezervare
from Domain.rezervareValidator import RezervareValidator
from Repository.json_repository import JsonRepository


class RezervareService:
    def __init__(self, rezervareRepository: JsonRepository, rezervareValidator: RezervareValidator,
                 locatieRepository: JsonRepository):
        self.rezervareRepository = rezervareRepository
        self.rezervareValidator = rezervareValidator
        self.locatieRepository = locatieRepository

    def getAll(self):
        return self.rezervareRepository.read()
    def adauga(self, idRezervare, nume, start, final, nr_oaspeti, id_locatie):
        '''
        Adauga o rezervare in multimea de rezervari
        :param idRezervare: id-ul rezervarii
        :param nume: numele rezervarii
        :param start: data de start a rezervarii
        :param final: data de final a rezervarii
        :param nr_oaspeti: numarul de oaspeti
        :param id_locatie: id-ul locatiei
        :return:
        '''
        if self.locatieRepository.read(id_locatie) is None:
            raise KeyError("NU exista o locatie cu id-ul dat!")
        rezervatie = Rezervare(idRezervare, nume, start, final, nr_oaspeti, id_locatie)
        self.rezervareValidator.valideaza(rezervatie)
        self.rezervareRepository.create(rezervatie)

    def OrdoneazaDescrescator(self, cat):
        '''
        Ordoneaza descrescator locatiile de o anumita categorie descrescator dupa tarif
        :param cat: categoria care se da de la tastatura, dupa ea cautam locatiile
        :return: o lista ordonata descrescator.
        '''
        dictionar = {}
        rezultat = []
        for locatie in self.locatieRepository.read():
            if cat == locatie.categorie:
                dictionar[locatie.id_entity] = locatie.tarif
        for iddict in dictionar:
            locatie = self.locatieRepository.read(iddict)
            rezultat.append({
                "locatie":self.locatieRepository.read(iddict),
                "tarif": locatie.tarif
            })
        return sorted(rezultat, key=lambda x: x["tarif"], reverse=True)

    def NrTotalDeOaspeti(self):
        '''
        Pentru fiecare categorie afiseaza nr total de oaspeti
        :return: o lista de dictionare
        '''
        dictionar = {}
        for locatie in self.locatieRepository.read():
            dictionar[locatie.categorie] = 0
        for rezervare in self.rezervareRepository.read():
            locatie = self.locatieRepository.read(rezervare.id_locatie)
            dictionar[locatie.categorie] += rezervare.nr_oaspeti
        rezultat = []
        for categorie in dictionar:
            rezultat.append({
                "cat":categorie,
                "nr": dictionar[categorie]
            })
        return rezultat
    def exportJson(self, filename):
        '''
        export json
        :param filename:
        :return:
        '''
        dictionar = {}
        for locatie in self.locatieRepository.read():
            dictionar[locatie.nume] = []
        for rezervare in self.rezervareRepository.read():
            loc = self.locatieRepository.read(rezervare.id_locatie)
            dictionar[loc.nume].append(rezervare.nume)
        with open(filename, "w") as f:
            f.write(jsonpickle.dumps(dictionar))
