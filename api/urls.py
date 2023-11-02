from django.urls import path
from api.views import ChickenPriceView

urlpatterns = [
    path('chicken-price/', ChickenPriceView.as_view()),
]