from django.urls import path
from users.views import UsersReadWriteView, UserGetUpdateDeleteView

urlpatterns = [
    path('users', UsersReadWriteView.as_view()),
    path('users/<int:pk>', UserGetUpdateDeleteView.as_view())
]
