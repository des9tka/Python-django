from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarPhotoSerializer, CarsSerializer


class CarView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAuthenticated(),

    def get_queryset(self):
        query = self.request.query_params.dict()

        queryset = super().get_queryset()

        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)

        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer


class AddCarPhotoView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        car = self.get_object()
        files = self.request.FILES
        for file in files:
            serializer = CarPhotoSerializer(data={'photo': files[file]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarsSerializer(car)
        return Response(serializer.data, status.HTTP_201_CREATED)

