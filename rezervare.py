from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Rezervare(Entity):
    nume: str
    start: str
    final: str
    nr_oaspeti: int
    id_locatie: str
