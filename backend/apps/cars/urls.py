from django.urls import path

from backend.apps.cars.views import AddCarPhotoView, CarRetrieveUpdateDestroyView, CarView

urlpatterns = [
    path('', CarView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photo', AddCarPhotoView.as_view())
]
