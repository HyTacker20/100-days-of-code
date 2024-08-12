from scraper import ApartmentsScraper
from google_forms_bot import GoogleFormsBot

if __name__ == '__main__':
    rent_site_url = "https://appbrewery.github.io/Zillow-Clone/"
    google_forms_url = ("https://docs.google.com/forms/d/e/1FAIpQLSfxUn-swsTUIlLtQqAxUvvv95rrNNFT_R9TKkn52C5PDYP1Jw"
                        "/viewform?fbzx=5684312670216844164")

    scrapper = ApartmentsScraper(rent_site_url)
    apartment_data_list = scrapper.parse_apartments_data()

    google_forms_bot = GoogleFormsBot()
    google_forms_bot.fill_form(google_forms_url, apartment_data_list)
