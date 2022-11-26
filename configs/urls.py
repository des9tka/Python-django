from django.urls import path
from users.views import UsersReadWriteView

urlpatterns = [
    path('users', UsersReadWriteView.as_view())
]
