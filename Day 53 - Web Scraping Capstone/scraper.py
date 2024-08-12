from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, Tag


@dataclass
class Apartment:
    adress: str
    price: str
    link: str


class ApartmentsScraper:
    def __init__(self, url: str):
        self.url = url

    @staticmethod
    def _get_website_content(link: str):
        response = requests.get(link)
        return response.content

    @staticmethod
    def _format_prices(price_list: list[Tag]) -> list[str]:
        formatted_price_list = []

        for price in price_list:
            print(price.text)
            print("+" in price.text)
            print(price.text.split("+")[0] if "+" in price else price.text.split("/")[0])
            formatted_price = price.text.split("+")[0] if "+" in price else price.text.split("/")[0]
            formatted_price_list.append(formatted_price)

        return formatted_price_list

    @staticmethod
    def _format_addresses(address_list: list[Tag]) -> list[str]:
        formatted_address_list = []
        for address in address_list:
            formatted_address = address.text.strip()
            formatted_address_list.append(formatted_address)

        return formatted_address_list

    @staticmethod
    def _format_links(link_list: list[Tag]) -> list[str]:
        formatted_link_list = []
        for link in link_list:
            formatted_link = link.attrs.get("href")
            formatted_link_list.append(formatted_link)

        return formatted_link_list

    def parse_apartments_data(self) -> list[Apartment]:
        content = self._get_website_content(self.url)
        soup = BeautifulSoup(content, "html.parser")

        addresses = list(soup.find_all("address"))
        prices = list(soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine"))
        links = list(soup.find_all("a", class_="StyledPropertyCardDataArea-anchor"))

        formatted_prices = self._format_prices(prices)
        formatted_addresses = self._format_addresses(addresses)
        formatted_links = self._format_links(links)

        apartments_list = [Apartment(address, price, link) for address, price, link in
                           zip(formatted_addresses, formatted_prices, formatted_links)]

        return apartments_list


if __name__ == '__main__':
    scraper = ApartmentsScraper("https://appbrewery.github.io/Zillow-Clone/")
    scraper.parse_apartments_data()
