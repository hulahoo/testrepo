from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mainapp.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index-page'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('posts/', include('mainapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)