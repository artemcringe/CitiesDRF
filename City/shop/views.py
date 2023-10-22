from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from .serializers import *


class CityLISTAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetListAPIView(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['pk']
        return Street.objects.filter(city_id=city_id)


class ShopCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def post(self, request, *args, **kwargs):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({"message": instance.id}, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get_queryset(self):
        qs = super().get_queryset()
        city = self.request.query_params.get('city')
        street = self.request.query_params.get('street')
        is_open = self.request.query_params.get('open')

        if city and street:
            qs = Shop.objects.filter(city__city_name__icontains=city, street__street_name__icontains=street)
        elif city:
            qs = Shop.objects.filter(city__city_name__icontains=city)
        elif street:
            qs = Shop.objects.filter(street__street_name__icontains=street)

        now = datetime.now().time()

        if is_open == "1":
            qs = qs.filter(open__lte=now, close__gte=now)
        elif is_open == "0":
            qs = qs.exclude(open__lte=now, close__gte=now)

        return qs


