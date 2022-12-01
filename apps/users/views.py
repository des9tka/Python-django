from apps.users.serializers import CarsSerializer
from apps.users.models import CarModel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CarView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer
