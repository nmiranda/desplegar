from django.conf.urls import url

from aero_scraper import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]