from django.urls import path

from apps.users.views import CarView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars', CarView.as_view()),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]
