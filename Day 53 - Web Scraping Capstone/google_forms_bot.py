import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from scraper import Apartment


class GoogleFormsBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def fill_form(self, url: str, apartments_data: list[Apartment]):
        self.driver.get(url)

        for apartment in apartments_data:
            address_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                        '1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                      '2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                                     '3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            send_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div['
                                                                      '1]/div[1]/div')
            time.sleep(0.1)

            address_field.send_keys(apartment.adress)
            price_field.send_keys(apartment.price)
            link_field.send_keys(apartment.link)
            send_button.click()

            time.sleep(0.5)

            back_button = self.driver.find_element(by=By.LINK_TEXT, value="Надіслати іншу відповідь")
            back_button.click()

            time.sleep(0.5)


if __name__ == '__main__':
    bot = GoogleFormsBot()
    bot.fill_form("https://docs.google.com/forms/d/e/1FAIpQLSfxUn-swsTUIlLtQqAxUvvv95rrNNFT_R9TKkn52C5PDYP1Jw/viewform",
                  [Apartment("test", "test", "test")])
