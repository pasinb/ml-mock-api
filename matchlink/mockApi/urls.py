from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'mockApi'
uuid_regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

router = DefaultRouter()
router.register(r'users', ScmUserViewset)

urlpatterns = [
    url(r'^nsme-ws/api/', include(router.urls)),
]
