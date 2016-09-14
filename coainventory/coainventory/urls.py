from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from inventory.views import *
from api.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'computers', ComputerViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'departments', DepartmentViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('inventory.urls')),
    url(r'^', include('login.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
