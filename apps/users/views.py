from apps.users.serializers import CarsSerializer
from apps.users.models import CarModel
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView


class CarView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()

        queryset = super().get_queryset()

        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)

        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarsSerializer


