import httpx
from selectolax.parser import HTMLParser
from api.functions import save_chicken_price
from datetime import date

def scrape_chicken_price():

    URL = "https://www.vda-ooigem.be/nl/marktprijzen/braadkippen"

    response = httpx.get(URL)

    if response.status_code == 200:
        html = HTMLParser(response.text)

        price_row = html.css("div.Row--withGutter")[1]

        contents = price_row.css("p")

        week = contents[0].text()
        scraped_date = contents[1].text()
        deinze = contents[2].text()
        abc = contents[3].text()

        prices = {
            "week": week,
            "date": scraped_date,
            "deinze": deinze.replace(",", "."),
            "abc": abc.replace(",", ".")
        }

        scraped_date_splitted = scraped_date.split("/")

        if date(scraped_date_splitted[2], scraped_date_splitted[1], scraped_date_splitted[0]) > date.today():
           return 
        else:
            save_chicken_price(prices)
