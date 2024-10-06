# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

This project involves querying an API to retrieve a list of countries and their past political leaders. Using this information, we scrape Wikipedia to extract and sanitize the first paragraph of each leader's biography. Finally, we store the collected data in a JSON file on disk for further use.

![coworking_img](https://grepsr.com/wp-content/uploads/2023/07/Creative-1.jpg)

## 📦 Repo structure

```
.
├── src/
│   ├── scraper.py
│   
├── .gitignore
├── main.py
├── leaders_data.json
├──requirements.txt 
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

3. Install the required modules as mentioned in the Requirements file.


##  Future Improvements
1. Add error handling for failed Wikipedia requests.

2. Optimize scraping to avoid making repeated requests to the same Wikipedia page.

3.Enhance the data sanitization process to clean up the text further


    ```
    python main.py
    ```


```python

# Instantiate an object called scraper from WikipediaScraper after importing it.
scraper = WikipediaScraper()

# The list of countries has to be created firstly by using get_countries() method from scraper object
countries = scraper.get_countries()

### Using these methods from scraper.py

def refresh_cookie(self)
    #This method is used for creating the cookies
       
def get_leaders(self, country: str)
    #This method is used for extracting the leader info based on country key.

def get_first_paragraph(self, wikipedia_url: str) -> str:
    #Scrapes and returns the first paragraph of each leader 

def to_json_file(self, filepath: str)
    #Storing the data structure (leaders and paragraphs) into a JSON file.
        
```
## ⏱️ Timeline

This project took three days and half  for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/moustafa-gabil-8a4a6bab/).

