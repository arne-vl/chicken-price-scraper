from rest_framework.views import APIView
from rest_framework.response import Response
from api.functions import get_most_recent_chicken_price


class ChickenPriceView(APIView):
    def get(self, request):
        return Response(
            get_most_recent_chicken_price()
        )