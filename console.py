from Service.locatieService import LocatieService
from Service.rezervareService import RezervareService


class Console:
    def __init__(self, locatieService: LocatieService, rezervareService: RezervareService):
        self.locatieService = locatieService
        self.rezervareService = rezervareService

    def runMenu(self):
        while True:
            print("1. Adauga o locatie ")
            print("2. Adauga o rezervare ")
            print("3. Afiseaza locatiile in ordinea descrescatoare a tarifului ")
            print("4. Afiseaza nr total de oaspeti pt fiecare categorie ")
            print("5. Export Json")
            print("a1. Afisare locatii ")
            print("a2. Afisare rezervari ")
            print("x. Iesire ")
            optiune = input("Dati optiunea ")
            if optiune == "1":
                self.uiAdaugaLocatie()
            elif optiune == "2":
                self.uiAdaugaRezervare()
            elif optiune == "3":
                cat = input("Dati categoria dupa care sa cautam locatiile ")
                self.afiseaza(self.rezervareService.OrdoneazaDescrescator(cat))
            elif optiune == "4":
                self.afiseaza(self.rezervareService.NrTotalDeOaspeti())
            elif optiune == "5":
                self.exportJson()
            elif optiune == "a1":
                self.afiseaza(self.locatieService.getAll())
            elif optiune == "a2":
                self.afiseaza(self.rezervareService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def uiAdaugaLocatie(self):
        try:
            idLlocatie = input("Dati id-ul locatiei ")
            nume = input("Dati numele locatiei ")
            categorie = input("Dati categoria locatiei ")
            tarif = float(input("Dati tariful locatiei "))
            capacitate = int(input("Dati capacitatea locatiei "))
            self.locatieService.adauga(idLlocatie, nume, categorie, tarif, capacitate)
        except Exception as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def uiAdaugaRezervare(self):
        try:
            idRezervare = input("Dati id-ul rezervarii ")
            nume = input("Dati numele oaspetuelui principal ")
            data_start = input("Dati data de inceput ")
            data_final = input("Dati data de final ")
            nr_oaspeti = int(input("Dati numarul de oaspeti "))
            id_locatie = input("Dati id-ul locatiei ")
            self.rezervareService.adauga(idRezervare, nume, data_start, data_final, nr_oaspeti, id_locatie)
        except Exception as e:
            print(e)

    def exportJson(self):
        try:
            filename = input("Dati numele fisierului: ")

            self.rezervareService.exportJson(filename)
        except Exception as e:
            print(e)

