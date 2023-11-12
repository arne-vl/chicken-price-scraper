import httpx
from selectolax.parser import HTMLParser
from api.functions import save_chicken_price

def scrape_chicken_price():

    URL = "https://www.vda-ooigem.be/nl/marktprijzen/braadkippen"

    response = httpx.get(URL)

    if response.status_code == 200:
        html = HTMLParser(response.text)

        price_row = html.css("div.Row--withGutter")[1]

        contents = price_row.css("p")

        week = contents[0].text()
        date = contents[1].text()
        deinze = contents[2].text()
        abc = contents[3].text()

        prices = {
            "week": week,
            "date": date,
            "deinze": deinze.replace(",", "."),
            "abc": abc.replace(",", ".")
        }

        if week > date.today().strftime("%W"):
           return 

        save_chicken_price(prices)
