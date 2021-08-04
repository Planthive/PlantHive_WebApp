from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='local-home'),
    path('output', views.output, name='script'),
]
