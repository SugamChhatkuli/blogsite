from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('api/accounts/', include('drf_registration.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
