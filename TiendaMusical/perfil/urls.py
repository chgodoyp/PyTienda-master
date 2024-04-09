from django.urls import path

from django.conf import settings

from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('perfil/', perfil, name='perfil'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 