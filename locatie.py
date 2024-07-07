from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Locatie(Entity):
    nume: str
    categorie: str
    tarif: float
    capacitate: int
