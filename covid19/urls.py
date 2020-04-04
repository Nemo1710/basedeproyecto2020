from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'covid19/$', views.index),
]
