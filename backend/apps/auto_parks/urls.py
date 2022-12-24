from django.urls import path

from .views import AutoParkListCreateView, CarListCreateView, RetrieveAutoParkView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', CarListCreateView.as_view()),
    path('/<int:pk>', RetrieveAutoParkView.as_view())
]