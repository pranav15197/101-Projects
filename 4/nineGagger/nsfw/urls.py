from django.conf.urls import patterns, url

from nsfw import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
