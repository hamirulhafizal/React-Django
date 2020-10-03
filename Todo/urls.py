from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers  # add this
from Todo import views  # add this
from . import views
from django.views.generic import TemplateView

urlpatterns = [
                  path(r'', TemplateView.as_view(template_name='index.html')),
                  path(r'admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
