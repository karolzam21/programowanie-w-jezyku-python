import requests
url = 'https://api.openbrewerydb.org/v1/breweries?per_page='
LbBrowarow = 20

class Brewery:
    id: str
    name: str
    brewery_type = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor',
                    'closed']
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: int
    latitude: int
    phone: str
    website_url: str
    state: str
    street: str

    def __init__(self, brewery):
        self.id = brewery.get("id")
        self.name = brewery.get("name")
        self.brewery_type = brewery.get("brewery_type")
        self.address_1 = brewery.get("brewery_type")
        self.address_2 = brewery.get("address_2")
        self.address_3 = brewery.get("address_3")
        self.city = brewery.get("city")
        self.state_province = brewery.get("state_province")
        self.postal_code = brewery.get("postal_code")
        self.country = brewery.get("country")
        self.longitude = brewery.get("state_province")
        self.latitude = brewery.get("latitude")
        self.phone = brewery.get("phone")
        self.website_url = brewery.get("website_url")
        self.state = brewery.get("state")
        self.street = brewery.get("street")

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

def main():
    res = requests.get(url + str(LbBrowarow))
    breweries = res.json()
    bw = []
    i = 0

    for b in breweries[:LbBrowarow]:
        bw.append(Brewery(brewery=b))
        print(f"{chr(27)}[4m {i + 1} - {str(b['name'])} {chr(27)}[0m \n" + str(bw[i]))
        i = i + 1

if __name__ == '__main__':
    main()