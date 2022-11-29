from django.urls import path

from apps.users.views import CarView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]
