from django.urls import path
from users.views import UserListView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path("users", UserListView.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateDeleteView.as_view())
]
