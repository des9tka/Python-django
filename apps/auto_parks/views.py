from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import AutoParksSerializer
from .models import AutoParksModel
from apps.users.serializers import CarsSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParksSerializer


class AddCarToAutoParkView(GenericAPIView):
    queryset = AutoParksModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        print(auto_park)
        data = self.request.data
        serializer = CarsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParksSerializer(auto_park)
        return Response(serializer.data)



