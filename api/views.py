from rest_framework.views import APIView
from rest_framework.response import Response
from api.functions import get_most_recent_price
from scraper.vda_scraper import scrape_price


class ChickenPriceView(APIView):
    def get(self, request):
        scrape_price()
        
        return Response(
            get_most_recent_price()
        )