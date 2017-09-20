"""food_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from backapp import views,account


urlpatterns = [
    url(r'^index/', account.index),
    url(r'^user_info/$', account.user_info),
    url(r'^user_group/$', account.user_group),
    url(r'^userdel_(\d+)/$', account.userdel),
    url(r'^useredit/$', account.useredit),
    url(r'^logout/$', account.logout),
    url(r'^useredit_ajax/$', account.useredit_ajax),
    url(r'^userdetail_(\d+)/$', account.userdetail),
    url(r'^table_manage/$', views.table_manage),
    url(r'^food_manage/$', views.food_manage),
    url(r'^foodtype_manage/$', views.foodtype_manage),
    url(r'^restaurant_order/$', views.restaurant_order),

]
