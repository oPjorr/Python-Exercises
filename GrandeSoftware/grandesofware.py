from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Guitar:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price
        
    def get_spec(self):
        return self.spec
    
class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood):    
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood
        
    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood
    
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serialNumber, price, guitar_spec):
        guitar = Guitar(serialNumber, price, guitar_spec)
        self.guitars.append(guitar)

    def get_guitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        matching_guitars = []
        for guitar in self.guitars:
            if search_guitar.get_builder() != guitar.get_spec().get_builder():
                continue
            model = search_guitar.get_model().lower()
            if model and model != "" and model != guitar.get_spec().get_model().lower():
                continue
            if search_guitar.get_typeg() != guitar.get_spec().get_typeg():
                continue
            if search_guitar.get_back_wood() != guitar.get_spec().get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_spec().get_top_wood():
                continue
            matching_guitars.append(guitar)

        return matching_guitars

inventory = Inventory()

inventory.add_guitar("V95693", 1499.95, GuitarSpec(
        Builder.FENDER.value,
        "Stratocastor",
            TypeG.ELETRIC.value,
            Wood.ALDER.value,
            Wood.ALDER.value,
        )
    )

inventory.add_guitar(
    "V55206",
    1329.79,
        GuitarSpec(
            Builder.FENDER.value,
            "Telecaster",
            TypeG.ELETRIC.value,
            Wood.CEDAR.value,
            Wood.MAPLE.value,
        )
    )

inventory.add_guitar(
    "V95393",
    1195.49,
    GuitarSpec(
        Builder.FENDER.value,
        "Stratocastor",
        TypeG.ELETRIC.value,
        Wood.ALDER.value,
        Wood.ALDER.value,
    )
)

whatErinLikes = GuitarSpec(
    Builder.FENDER.value,
    "Stratocastor",
    TypeG.ELETRIC.value,
    Wood.ALDER.value,
    Wood.ALDER.value,
)

found_guitars = inventory.search_guitar(whatErinLikes)
if found_guitars:
    print("Erin, talvez você goste dessas guitarras:")
    for guitar in found_guitars:
        print(f"\n{guitar.get_spec().get_builder()} {guitar.get_spec().get_model()} {guitar.get_spec().get_typeg()} guitar, ela tem:\n{guitar.get_spec().get_back_wood()} na traseira e laterais e {guitar.get_spec().get_top_wood()} no tampo.\nEla pode ser sua por apenas US${guitar.get_price()}!")
else:
  print("Desculpe Erin, não temos nada para você")