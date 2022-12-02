from django.urls import path

from .views import AutoParkListCreateView, AddCarToAutoParkView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view())
]