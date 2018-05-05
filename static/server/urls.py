from django.conf.urls import url
from django.contrib import admin
from account import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^account/register/$', views.register),
    url(r'^account/login/$',views.login),
    url(r'^account/logout$', views.logout)
]