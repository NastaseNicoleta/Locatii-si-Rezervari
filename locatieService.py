from Domain.locatie import Locatie
from Domain.locatieValidator import LocatieValidator
from Repository.json_repository import JsonRepository


class LocatieService:
    def __init__(self, locatieRepository: JsonRepository, locatieValidator: LocatieValidator):
        self.locatieRepository = locatieRepository
        self.locatieValidator = locatieValidator

    def getAll(self):
        return self.locatieRepository.read()

    def adauga(self, idLocatie, nume, categorie, tarif, capacitate):
        '''
        Adauga o locatie in multimea de locatii
        :param idLocatie: id-ul locatiei
        :param nume: numele locatiei
        :param categorie: categoria locatiei
        :param tarif: tariful locatiei
        :param capacitate: capacitatea locatiei
        :return:
        '''
        locatie = Locatie(idLocatie, nume, categorie, tarif, capacitate)
        self.locatieValidator.valideaza(locatie)
        self.locatieRepository.create(locatie)
