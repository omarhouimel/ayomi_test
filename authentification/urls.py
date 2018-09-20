from sys import path

from django.conf.urls import url
from django.contrib import admin

from authentification import views

urlpatterns = [
    # path('admin/', admin.site.urls),
     url('details',views.details,name='details'),
     url('', views.index,name='index'),


]
