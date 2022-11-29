from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.serializers import CarsSerializer
from apps.users.models import CarModel


class CarView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarsSerializer(instance=cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarsSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDestroyView(APIView):

    def det_bu_id(self, pk):


    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        get = CarModel.objects.get(pk=pk)
        serializer = CarsSerializer(instance=get)
        return Response(serializer.data, status.HTTP_200_OK)
