from configs import settings

from django.conf.urls.static import static
from django.urls import include, path

import rest_framework.exceptions
from rest_framework.exceptions import bad_request, server_error

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'