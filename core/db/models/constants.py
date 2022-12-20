from enum import Enum


class UserType(str, Enum):
    CLEANER = "Cleaner"
    CUSTOMER = "Customer"


class Gender(str, Enum):
    HOMME = "Homme"
    FEMME = "Femme"


class City(str, Enum):
    BOUAKE = "Bouaké"


class Street(str, Enum):
    AIR_FRANCE_1 = "Air France 1"
    AIR_FRANCE_2 = "Air France 2"
    AIR_FRANCE_3 = "Air France 3"
    AHOUGNANSOU = "Ahougnansou"
    BROUKRO = "Broukro"
    BEAUFORT = "Beaufort"
    CIDT = "Cité CIDT"
    COMMERCE = "Commerce"
    CORRIDOR_SUD = "Corridor SUD"
    CORRIDOR_NORD = "Corridor NORD"
    DARES_SALAM = "Dares Salam"
    HABITAT = "Habitat de la caisse"
    HOUPHOUET_VILLE = "Houphouet Ville"
    KENNEDY = "Kennedy"
    KOKO = "Koko"
    MUNICIPAL = "Municipal"
    NGATTAKRO = "N'GATTAKRO"
    NDAKRO = "N'Dakro"
    NIMBO = "Nimbo"
    ZONE = "Zone"
