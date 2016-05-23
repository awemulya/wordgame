from django.conf.urls import url

from words import views

app_name = "words"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^play', views.play, name='play'),
]