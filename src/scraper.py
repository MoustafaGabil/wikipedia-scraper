import requests
from bs4 import BeautifulSoup
import json
class WikipediaScraper:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = None

    def refresh_cookie(self):
        self.cookie = requests.get(f"{self.base_url}{self.cookies_endpoint}").cookies

    def get_countries(self):
        countries_url = f"{self.base_url}{self.country_endpoint}"
        self.countries = requests.get(countries_url, cookies=self.cookie).json()
        return self.countries

    def get_leaders(self, country: str):
        leaders_per_country = {}
        leaders_url = f"{self.base_url}{self.leaders_endpoint}"
        for country in self.countries:
            leaders_list = requests.get(leaders_url, cookies=self.cookie, params={"country": country})
            leaders_per_country[country] = leaders_list.json()
        self.leaders_data = leaders_per_country   

    def get_first_paragraph(self, wikipedia_url: str):
        r = requests.get(wikipedia_url)
        soup = BeautifulSoup(r.content, "html.parser")
        paragraphs = soup.find_all("p")

        for paragraph in paragraphs:
            if paragraph.find("b"):
                first_paragraph = paragraph.text

                break
        return first_paragraph

    def get_leader_paragraphs(self):
        list_leaders_urls = []
        for country, leaders in self.leaders_data.items():
            for items in leaders:
                url = items["wikipedia_url"]
                list_leaders_urls.append(url)
        for url in list_leaders_urls:
            return self.get_first_paragraph(url))
        
############################################################### It is not the final version #########################################
scraper = WikipediaScraper()
scraper.refresh_cookie()



