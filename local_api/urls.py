# myapi/urls.pyfrom django.urls import include, path
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'growth_schedule', views.Growth_scheduleViewSet)
router.register(r'manual_schedule', views.Manual_scheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
