from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ActivateUserView, RecoveryRequestView, RecoveryPasswordView


urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoveryRequestView.as_view()),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view())
]