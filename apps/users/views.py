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

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = CarModel.objects.filter(pk=pk).exists()

        if not exist:
            return Response('Not found', status.HTTP_400_BAD_REQUEST)

        get = CarModel.objects.get(pk=pk)
        serializer = CarsSerializer(instance=get)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        exist = CarModel.objects.filter(pk=pk).exists()

        if not exist:
            return Response('Not found', status.HTTP_400_BAD_REQUEST)

        car = CarModel.objects.get(pk=pk)
        serializer = CarsSerializer(car, data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        exist = CarModel.objects.filter(pk=pk).exists()

        if not exist:
            return Response('Not found', status.HTTP_400_BAD_REQUEST)

        car = CarModel.objects.get(pk=pk)
        serializer = CarsSerializer(car, data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = CarModel.objects.filter(pk=pk).exists()

        if not exist:
            return Response('Not found', status.HTTP_400_BAD_REQUEST)

        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




