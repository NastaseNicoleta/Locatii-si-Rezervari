from Domain.locatieValidator import LocatieValidator
from Domain.rezervareValidator import RezervareValidator
from Repository.json_repository import JsonRepository
from Service.locatieService import LocatieService
from Service.rezervareService import RezervareService
from UserInterface.console import Console


def main():
    locatieRepository = JsonRepository("locatie.json")
    locatieValidator = LocatieValidator()
    locatieService = LocatieService(locatieRepository, locatieValidator)


    rezervareRepository = JsonRepository("rezervare.json")
    rezervareValidator = RezervareValidator()
    rezervareService = RezervareService(rezervareRepository, rezervareValidator, locatieRepository)

    console = Console(locatieService, rezervareService)
    console.runMenu()


if __name__ == '__main__':
    main()
