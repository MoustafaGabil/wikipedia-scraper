from src.scraper import WikipediaScraper


def main():
    # Instantiate an object called scraper from WikipediaScraper after importing it.
    scraper = WikipediaScraper()

    # The list of countries has to be created firstly by using get_countries() method from scraper object
    countries = scraper.get_countries()

    # Looping over each country in the country list to extract each leader data.
    for country in countries:
        print(f"Scraping leaders for: {country}")
        scraper.get_leaders(country)

        # For each leader in leaders_data attribute, the Wikipedia first paragraph can be extracted based on the county (as key)
        # Note: the scraper.leaders_data is a dic so the key has to be specified (the same country from the above loop)
        for leader in scraper.leaders_data[country]:
            wikipedia_url = leader.get("wikipedia_url")
            paragraph = scraper.get_first_paragraph(
                wikipedia_url
            )  # passing the wikipedia_url to get_first_paragra() method
            leader["wikipedia_first_paragraph"] = (
                paragraph  # Adding the extracted paragraph to the leader data uner the name:wikipedia_first_paragraph
            )
            # note that, leader is a dic so,the paragraph has to be added in this way

    # Save all the data into a JSON file
    scraper.to_json_file("leaders_data.json")
    print("Data has been saved to leaders_data.json")


if __name__ == "__main__":
    main()
