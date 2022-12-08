from django.urls import include, path

import apps.users.urls

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls'))
]
