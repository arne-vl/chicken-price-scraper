from price_quotation.models import PriceQuotation
from scraper.change_date_format import change_date_format

def get_most_recent_price() -> dict:
    ordered = PriceQuotation.objects.order_by("-date")
    recent = ordered[0]

    if len(ordered) == 1:
        return {
            "week": recent.week,
            "date": recent.date,
            "deinze": f"€ {recent.deinze}",
            "abc": f"€ {recent.abc}",
        }

    previous = ordered[1]
    return {
        "week": recent.week,
        "date": recent.date,
        "deinze": f"€ {recent.deinze} ({(recent.deinze - previous.deinze):.2f})",
        "abc": f"€ {recent.abc} ({(recent.abc - previous.abc):.2f})",
    }

def save_price(prices: dict):
    if prices["abc"] == "":
        previous_quotation = PriceQuotation.objects.order_by("-date")[0]
        prices["abc"] = previous_quotation.abc
    
    if prices["deinze"] == "":
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
        pc = PriceQuotation.objects.filter(
            week=prices["week"], date=change_date_format(prices["date"])
        ).first()

        if pc.deinze != prices["deinze"] or pc.abc != prices["abc"]:
            pc.deinze = prices["deinze"]
            pc.abc = prices["abc"]
            pc.save()
            
    else:
        PriceQuotation.save(price_quotation)