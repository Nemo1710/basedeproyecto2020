from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'inicio/$', views.inicio),
]
