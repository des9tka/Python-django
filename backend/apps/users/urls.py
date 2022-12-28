from django.urls import path

from .views import (
    AdminToUserView,
    AutoParksListCreateView,
    AvatarCreateView,
    UserActivateView,
    UserCreateView,
    UserDeactivateView,
    UserListView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),
    path('/auto_parks', AutoParksListCreateView.as_view()),
    path('/avatar', AvatarCreateView.as_view()),
]
