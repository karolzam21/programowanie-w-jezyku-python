from typing import List

class Brewery:
    def __init__(self, name):
        self.name = name
        # TODO: add rest of arguments

    def __str__(self):
        # TODO: return string describing class
        pass


def get_breweries_from_api() -> list:
    '''
    TODO:
     1. import requests
     2. send GET request to the api: https://api.openbrewerydb.org/v1/breweries
     3. return list of breweries form API
    '''
    pass


def brewery_factory(breweries: list) -> List[Brewery]:
    # TODO: run loop over all breweries to create list of Brewery
    pass


def main():
    breweries = get_breweries_from_api()
    breweries = brewery_factory(breweries)

    # TODO: loop over all breweries and display each of them


main()