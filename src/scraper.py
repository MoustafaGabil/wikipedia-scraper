import requests
from bs4 import BeautifulSoup
import json


class WikipediaScraper:
    """This class will be used to creat an object to scrape the each countrys' leader to extract the information about them like First name, last name, date"""

    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}  # creating this dic to be filled later with the target data
        self.cookie = None

    def refresh_cookie(self):
        """This method is used for creating the cookies each time to ensure the functionality of it
        as the cookies normally expire every 30 seconds."""
        self.cookie = requests.get(f"{self.base_url}{self.cookies_endpoint}").cookies

    def get_countries(self):
        """This method is used for creating  list of countries exisit in the website.
        The object is returned as a json file"""
        self.refresh_cookie()  # The cookies has to be activated each time when calling this method
        countries_url = f"{self.base_url}{self.country_endpoint}"
        countries = requests.get(countries_url, cookies=self.cookie).json()
        return countries

    def get_leaders(self, country: str):
        """This method is used for extracting the leader info based on country key.
        The results is then added to the leaders_data dic based on the country"""
        self.refresh_cookie()  # The cookies has to be activated each time when calling this method
        leaders_url = f"{self.base_url}{self.leaders_endpoint}"

        leaders_list = requests.get(
            leaders_url, cookies=self.cookie, params={"country": country}
        )
        self.leaders_data[country] = leaders_list.json()

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        """Scrapes and returns the first paragraph of each leader from the wikipedia url exists in each leader's data.
        Note: this method will be using by looping over leaders_data object for ech leader based on the country (key) to extract thewikipedia_url
            and passing the extracted URL to this method to get the first paragraph"""

        r = requests.get(wikipedia_url)

        soup = BeautifulSoup(r.content, "html.parser")
        paragraphs = soup.find_all("p")

        for paragraph in paragraphs:
            if paragraph.find("b"):
                return paragraph.text.strip()

    def to_json_file(self, filepath: str):
        """Storing the data structure (leaders and paragraphs) into a JSON file."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.leaders_data, f, ensure_ascii=False, indent=4)

    def __str__(self):
        """Returns a string representation of the WikipediaScraper object."""
        return (
            f"This class scraps the website: {self.base_url} to get the countries {self.get_countries()}' leaders''' info, "
            f"Such as':' First name, Last name, Date of birth,...etc"
        )
