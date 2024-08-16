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

class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"


class Style(Enum):
    A = "a"
    F = "f"


class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"


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

class InstrumentSpec:
    def __init__(self, properties=None):
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties.copy()

    def get_property(self, property_name):
        return self.properties.get(property_name)


    def get_properties(self):
        return self.properties

    def matches(self, other_spec):
        for property_name in other_spec.get_properties():
            if self.properties.get(property_name) != other_spec.get_property(property_name):
                return False
        return True
    
class Instrument:
    def __init__(self, serial_number, price, spec: InstrumentSpec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    @property
    def get_spec(self) -> InstrumentSpec:
        return self.spec
    
class Inventory:
    def __init__(self):
        self.inventory = []

    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

    def get_instrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec):
        matching_instruments = []
        for instrument in self.inventory:
            if instrument.get_spec.matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments

def initialize_inventory(inventory: Inventory) -> None:
    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.FENDER,
        "model": "stratocastor",
        "type": Type.ELECTRIC,
        "top_wood": Wood.ALDER,
        "back_wood": Wood.ALDER,
        "num_strings": 6,
    }

    inventory.add_instrument("V95693", 1499.97, InstrumentSpec(properties))
    inventory.add_instrument("V99999", 2174.49, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.MARTIN,
        "model": "Les Paul",
        "type": Type.ELECTRIC,
        "top_wood": Wood.MAHOGANY,
        "back_wood": Wood.ADIRONDACK,
        "num_strings": 6,
    }

    inventory.add_instrument("V22784", 5495.27, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.MANDOLIN,
        "builder": Builder.GIBSON,
        "model": "F5-G",
        "type": Type.ACOUSTIC,
        "top_wood": Wood.MAPLE,
        "back_wood": Wood.MAPLE,
        "style": Style.A,
    }

    inventory.add_instrument("V73832", 3459.99, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.BANJO,
        "builder": Builder.GIBSON,
        "model": "RB-3",
        "type": Type.ACOUSTIC,
        "num_strings": 5,
        "back_wood": Wood.MAPLE,
    }

    inventory.add_instrument("V46257", 674.49, InstrumentSpec(properties))
    inventory.add_instrument("V85121", 1597.95, InstrumentSpec(properties))

def show_instruments(matching_instruments: list[Instrument]):
    if matching_instruments:
        print("Erin, talvez você goste destas: ")
        for i, instrument in enumerate(matching_instruments, 1):
            instrument_spec = instrument.get_spec
            instrument_name = instrument_spec.get_property("instrument_type").value

            print(f"\n{i}. {instrument_name}: {instrument.get_serial_number()} {instrument_spec.get_property('builder').value} {instrument_spec.get_property('model')} {instrument_spec.get_property('type')}")
            for property_name, property_value in instrument_spec.get_properties().items():
                print(f"   - {property_name.capitalize()}: {property_value.value if isinstance(property_value, Enum) else property_value}")
            print(f"\n   - Ela possui o custo de US$ {instrument.get_price():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    properties = {
        "builder": Builder.GIBSON,
        "type": Type.ACOUSTIC,
        "back_wood": Wood.MAPLE,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.RYAN,
        "model": "Stratocastor",
        "type": Type.ACOUSTIC,
        "top_wood": Wood.CEDAR,
        "back_wood": Wood.SITKA,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.MARTIN,
        "type": Type.ELECTRIC,
        "top_wood": Wood.MAHOGANY,
        "back_wood": Wood.ADIRONDACK,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "type": Type.ELECTRIC,
        "top_wood": Wood.ALDER,
        "num_strings": 6,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.OLSON,
        "back_wood": Wood.ADIRONDACK,
        "style": Style.F,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

if __name__ == "__main__":
    main()