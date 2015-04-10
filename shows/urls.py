from django.conf.urls import patterns, url

from shows import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
    url(r'^add$', views.add, name='add'),
    url(r'^show/(?P<show_id>\d+)/$', views.show, name='show'),
)
