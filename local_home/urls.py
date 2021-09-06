from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

urlpatterns = [
    path('', views.home, name='local-home'),
    path('state', views.state, name='StartStop'),
    path('import', views.importData, name='ImportData'),
    path('export', views.exportData, name='ExportData'),

    #path('api/blabla/send', views.send, name='send'),
    #path('api/blabla/get', views.get, name='get'),

    #path('api/blabla/get', include('rest_framework.urls', namespace='rest_framework'))
]
