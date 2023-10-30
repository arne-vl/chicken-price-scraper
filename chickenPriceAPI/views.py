from rest_framework.views import APIView
from rest_framework.response import Response
from chickenPriceAPI.scraper.vda_scraper import get_most_recent_price


class ChickenPriceView(APIView):
    def get(self, request):
        return Response(
            get_most_recent_price()
        )
