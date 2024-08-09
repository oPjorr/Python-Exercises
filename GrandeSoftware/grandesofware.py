from enum import Enum
from abc import ABC, abstractmethod


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


class Style(Enum):
    A = "a"
    F = "f"


class Instrument(ABC):
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self) -> str:
        return self.serialNumber

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, new_price) -> None:
        self.price = new_price

    def getSpec(self):
        return self.spec


class InstrumentSpec(ABC):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
    ):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def getBuilder(self) -> Builder:
        return self.builder

    def getModel(self) -> str:
        return self.model

    def getTypeG(self) -> TypeG:
        return self.typeg

    def getBackWood(self) -> Wood:
        return self.back_wood

    def getTopWood(self) -> Wood:
        return self.top_wood

    @abstractmethod
    def matches(self, other_spec):
        pass


class GuitarSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
        num_strings,
    ):
        super().__init__(builder, model, typeg, back_wood, top_wood)
        self.num_strings = num_strings

    def getNumStrings(self):
        return self.num_strings

    def matches(self, other_spec):
        if not isinstance(other_spec, GuitarSpec):
            return False

        if self.builder != other_spec.getBuilder():
            return False
        if self.model and self.model.lower() != other_spec.getModel().lower():
            return False
        if self.typeg != other_spec.getTypeG():
            return False
        if self.back_wood != other_spec.getBackWood():
            return False
        if self.top_wood != other_spec.getTopWood():
            return False
        if self.num_strings != other_spec.getNumStrings():
            return False
        return True


class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, spec: GuitarSpec):
        super().__init__(serial_number, price, spec)


class MandolinSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
        style: Style,
    ):
        super().__init__(builder, model, typeg, back_wood, top_wood)
        self.style = style

    def getStyle(self):
        return self.style

    def matches(self, other_spec):
        if not isinstance(other_spec, MandolinSpec):
            return False

        if self.builder != other_spec.getBuilder():
            return False
        if self.model and self.model.lower() != other_spec.getModel().lower():
            return False
        if self.typeg != other_spec.getTypeG():
            return False
        if self.back_wood != other_spec.getBackWood():
            return False
        if self.top_wood != other_spec.getTopWood():
            return False
        if self.style != other_spec.getStyle():
            return False

        return True


class Mandolin(Instrument):
    def __init__(self, serial_number, price, spec: MandolinSpec):
        super().__init__(serial_number, price, spec)


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_instrument(self, serial_number, price, spec: GuitarSpec | MandolinSpec):
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)

        self.inventory.append(instrument)

    def get_instrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument

        return None

    def search(self, search_spec: GuitarSpec | MandolinSpec):
        results = []

        if isinstance(search_spec, GuitarSpec):
            for guitar in self.inventory:
                if isinstance(guitar, Guitar) and guitar.spec.matches(search_spec):
                    results.append(guitar)

        elif isinstance(search_spec, MandolinSpec):
            for mandolin in self.inventory:
                if isinstance(mandolin, Mandolin) and mandolin.spec.matches(
                    search_spec
                ):
                    results.append(mandolin)

        return results or None


def initializeInventory(inventory):
    spec1 = GuitarSpec(
        Builder.RYAN,
        "Stratocastor",
        TypeG.ACOUSTIC,
        Wood.CEDAR,
        Wood.SITKA,
        6,
    )

    inventory.add_instrument("V95693", 1499.95, spec1)

    spec2 = GuitarSpec(
        Builder.OLSON,
        "D-18",
        TypeG.ELETRIC,
        Wood.BRAZILIAN_ROSEWOOD,
        Wood.ADIRONDACK,
        6,
    )

    inventory.add_instrument("122784", 5495.95, spec2)

    spec3 = MandolinSpec(
        Builder.MARTIN,
        "D-18",
        TypeG.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.ADIRONDACK,
        Style.A,
    )

    inventory.add_instrument("V22784", 5495.95, spec3)

    spec4 = MandolinSpec(
        Builder.OLSON,
        "D-18",
        TypeG.ELETRIC,
        Wood.BRAZILIAN_ROSEWOOD,
        Wood.ADIRONDACK,
        Style.F,
    )

    inventory.add_instrument("V95694", 6299.95, spec4)


def show_instruments(matching_instruments: list[Guitar | Mandolin]):
    if matching_instruments:
        print("Erin, talvez você goste destas: ")
        for i, instrument in enumerate(matching_instruments, 1):
            instrument_spec = instrument.getSpec()
            instrument_name = instrument.__class__.__name__
            is_guitar = isinstance(instrument_spec, GuitarSpec)
            print(
                f"\n{i}. {instrument_name}: {instrument.getSerialNumber()} {instrument_spec.getBuilder().value} {instrument_spec.getModel()} {instrument_spec.getTypeG().value} {instrument_name}:".title(),
                f"\n   - {instrument_spec.getBackWood().value.capitalize()} na traseira e laterais",
                f"\n   - {instrument_spec.getTopWood().value.capitalize()} no tampo,",
                f"com {f'{instrument_spec.getNumStrings()} cordas' if is_guitar else f'o estilo {instrument_spec.getStyle().value.upper()}'}"
                f"\n   - Ela possui o custo de US$ {instrument.getPrice():.2f}!",
            )
    else:
        print("Desculpe Erin, não temos nada para você")


def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(
        Builder.RYAN,
        "Stratocastor",
        TypeG.ACOUSTIC,
        Wood.CEDAR,
        Wood.SITKA,
        6,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    whatErinLikes = GuitarSpec(
        Builder.OLSON,
        "D-18",
        TypeG.ELETRIC,
        Wood.BRAZILIAN_ROSEWOOD,
        Wood.ADIRONDACK,
        6,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    whatErinLikes = MandolinSpec(
        Builder.MARTIN,
        "D-18",
        TypeG.ACOUSTIC,
        Wood.MAHOGANY,
        Wood.ADIRONDACK,
        Style.A,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)

    whatErinLikes = MandolinSpec(
        Builder.OLSON,
        "D-18",
        TypeG.ELETRIC,
        Wood.BRAZILIAN_ROSEWOOD,
        Wood.ADIRONDACK,
        Style.F,
    )

    matching_instruments = inventory.search(whatErinLikes)
    show_instruments(matching_instruments)


if __name__ == "__main__":
    main()
