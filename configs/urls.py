from django.urls import include, path

import apps.users.urls

urlpatterns = [
    path('user', include(('apps.users.urls'))),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls'))
]
