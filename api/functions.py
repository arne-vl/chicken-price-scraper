from price_quotation.models import ChickenPriceQuotation
from scraper.change_date_format import change_date_format

def get_most_recent_chicken_price() -> dict:
    ordered = ChickenPriceQuotation.objects.order_by("-date")
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

def save_chicken_price(prices: dict):
    if prices["abc"] == "":
        previous_quotation = ChickenPriceQuotation.objects.order_by("-date")[0]
        prices["abc"] = previous_quotation.abc
    
    if prices["deinze"] == "":
        previous_quotation = ChickenPriceQuotation.objects.order_by("-date")[0]
        prices["deinze"] = previous_quotation.deinze

    price_quotation = ChickenPriceQuotation(
        week=prices["week"],
        date=change_date_format(prices["date"]),
        deinze=prices["deinze"],
        abc=prices["abc"],
    )

    if ChickenPriceQuotation.objects.filter(
        week=prices["week"], date=change_date_format(prices["date"])
    ).exists():
        pc = ChickenPriceQuotation.objects.filter(
            week=prices["week"], date=change_date_format(prices["date"])
        ).first()

        if pc.deinze != prices["deinze"] or pc.abc != prices["abc"]:
            pc.deinze = prices["deinze"]
            pc.abc = prices["abc"]
            pc.save()
            
    else:
        ChickenPriceQuotation.save(price_quotation)