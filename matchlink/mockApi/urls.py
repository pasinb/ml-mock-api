from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="MatchLink API")
from .views import *

app_name = 'mockApi'
uuid_regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

router = DefaultRouter()
router.register(r'users', ScmUserViewset)

urlpatterns = [
    url(r'^nsme-ws/api/', include(router.urls)),
    url(r'^api-docs/', schema_view)
]
