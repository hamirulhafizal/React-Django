from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers                    # add this
from Todo import views

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this

urlpatterns = [
                  path(r'', include('Todo.urls')),
                  path('api/', include(router.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
