from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.users.urls')),
    path('auto_parks', include('apps.auto_parks.urls'))
]
