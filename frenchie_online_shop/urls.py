from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('frenchie_online_shop.auth_app.urls')),
    path('', include('frenchie_online_shop.web.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
