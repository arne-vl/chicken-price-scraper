import httpx
from selectolax.parser import HTMLParser
import re


def get_most_recent_price():

    URL = "https://www.vda-ooigem.be/nl/marktprijzen/braadkippen"

    response = httpx.get(URL)
    html = HTMLParser(response.text)

    price_string = html.css("div.Row--withGutter")[1].text()

    week = price_string[:-28]
    date = price_string[-28:-18]
    deinze = price_string[-18:-12]
    abc = price_string[-12:-6]

    prices = {
        "week": week,
        "date": date,
        "deinze": "€" + deinze[:-2],
        "abc": "€" + abc[:-2],
    }

    return prices