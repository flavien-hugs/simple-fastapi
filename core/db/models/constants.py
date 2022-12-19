
from enum import Enum


class UserType(str, Enum):
    CLEANING = 'Ménage'
    CUSTOMER = 'Client'


class Gender(str, Enum):
    MAN = 'Homme'
    WOMEN = 'Femme'


class City(str, Enum):
    BKE = 'Bouaké'
