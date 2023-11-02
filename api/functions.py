from price_quotation.models import PriceQuotation
from scraper.change_date_format import change_date_format

def get_most_recent_price() -> dict:
    ordered = PriceQuotation.objects.order_by("-date")
    recent = ordered[0]
    previous = ordered[1]
    return {
        "week": recent.week,
        "date": recent.date,
        "deinze": f"€ {recent.deinze} ({(recent.deinze - previous.deinze):.2f})",
        "abc": f"€ {recent.abc} ({(recent.abc - previous.abc):.2f})",
    }

def save_price(prices: dict):
    if prices["abc"] == "xxxxxx":
        previous_quotation = PriceQuotation.objects.order_by("-date")[0]
        prices["abc"] = previous_quotation.abc
    
    if prices["deinze"] == "xxxxxx":
        previous_quotation = PriceQuotation.objects.order_by("-date")[0]
        prices["deinze"] = previous_quotation.deinze

    price_quotation = PriceQuotation(
        week=prices["week"],
        date=change_date_format(prices["date"]),
        deinze=prices["deinze"],
        abc=prices["abc"],
    )

    if PriceQuotation.objects.filter(
        week=prices["week"], date=change_date_format(prices["date"])
    ).exists():
        pass
    else:
        PriceQuotation.save(price_quotation)