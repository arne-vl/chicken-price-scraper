import httpx
from selectolax.parser import HTMLParser
from api.functions import save_price


def scrape_price():

    URL = "https://www.vda-ooigem.be/nl/marktprijzen/braadkippen"

    response = httpx.get(URL)

    if response.status_code == 200:
        html = HTMLParser(response.text)

        price_string = html.css("div.Row--withGutter")[1].text()

        while len(price_string) < 30:
            price_string += "x"

        week = price_string[:-28]
        date = price_string[-28:-18]
        deinze = price_string[-18:-12]
        abc = price_string[-12:-6]

        prices = {
            "week": week,
            "date": date,
            "deinze": deinze.replace(",", "."),
            "abc": abc.replace(",", ".")
        }

        save_price(prices)
