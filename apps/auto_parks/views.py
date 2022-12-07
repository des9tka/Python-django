from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import AutoParksSerializer
from .models import AutoParksModel
from apps.cars.serializers import CarsSerializer
from apps.cars.models import CarModel


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer


class CarListCreateView(GenericAPIView):
    queryset = AutoParksModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        cars = CarModel.objects.filter(auto_park=pk)
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParksSerializer(auto_park)
        return Response(serializer.data)


class RetrieveAutoParkView(GenericAPIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        cars = CarModel.objects.filter(auto_park=pk)
        serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)
