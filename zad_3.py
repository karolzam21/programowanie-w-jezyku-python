class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m²\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zł\n"
            f"Powierzchnia działki: {self.plot} m²"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m²\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zł\n"
            f"Piętro: {self.floor}"
        )


# Tworzenie obiektów
house = House(120, 5, 750000, "Warszawa, ul. Leśna 10", 500)
flat = Flat(60, 3, 450000, "Kraków, ul. Słoneczna 5", 3)

# Wyświetlanie obiektów
print(house)
print()
print(flat)
