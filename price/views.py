from rest_framework.views import APIView
from rest_framework.response import Response

from price.services.startech import StartechPriceService


class StartechPriceApiView(APIView):
    def get(self, request):
        #return Response("Hello")
        startech_price = StartechPriceService.get_price()
        return Response(startech_price)