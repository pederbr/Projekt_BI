from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('statistikk', views.statistikk, name='statistikk'),
    path('upload', views.upload, name='upload'),
    path('del_bedpres/', views.del_bedpres, name='del_bedpres'),
    path('statistikk_mal', views.statistikk_mal, name='statistikk_mal'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
