from backend.configs import settings

from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('cars', include('backend.apps.cars.urls')),
    path('auto_parks', include('backend.apps.auto_parks.urls')),
    path('users', include('backend.apps.users.urls')),
    path('auth', include('backend.apps.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'