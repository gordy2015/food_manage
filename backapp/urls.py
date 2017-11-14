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
from backapp import views,account,search_article


urlpatterns = [
    url(r'^index/', account.index),
    url(r'^user_info/$', account.userinfo),
    # url(r'^userdel_(\d+)/$', account.userdel),
    url(r'^userdel_ajax/$', account.userdel_ajax),
    url(r'^useredit_submit/$', account.useredit_submit),
    url(r'^logout/$', account.logout),
    url(r'^useredit_ajax/$', account.useredit_ajax),
    url(r'^userdetail_(\d+)/$', account.userdetail),

    url(r'^group_info/$', account.groupinfo),
    url(r'^groupdetail_(\d+)/$', account.groupdetail),
    url(r'^groupedit/$', account.groupedit),
    url(r'^groupdel_(\d+)/$', account.groupdel),

    url(r'^table_manage/$', views.table_manage),
    url(r'^tableedit_confirm/$', views.tableedit_confirm),
    url(r'^tableedit_ajax/$', views.tableedit_ajax),
    url(r'^table_del_ajax/$', views.table_del_ajax),

    url(r'^food_manage/$', views.food_manage),
    url(r'^food_add_ajax/$', views.food_add_ajax),
    url(r'^food_del_ajax/$', views.food_del_ajax),
    url(r'^foodedit_ajax/$', views.foodedit_ajax),
    url(r'^foodedit_confirm/$', views.foodedit_confirm),

    url(r'^foodtype_manage/$', views.foodtype_manage),
    url(r'^foodtype_add_ajax/$', views.foodtype_add_ajax),
    url(r'^foodtypeedit_confirm/$', views.foodtypeedit_confirm),
    url(r'^foodtypeedit_ajax/$', views.foodtypeedit_ajax),
    url(r'^foodtype_del_ajax/$', views.foodtype_del_ajax),

    url(r'^order/$', views.order),
    url(r'^order_detail-(?P<nid>\d+)/', views.order_detail),
    url(r'^order_add_ajax/$', views.order_add_ajax),
    url(r'^order_del_ajax/$', views.order_del_ajax),
    url(r'^order_comfirm_ajax/$', views.order_comfirm_ajax),

    url(r'^fc_del_ajax/$', views.fc_del_ajax),
    url(r'^fcount_comfirm/$', views.fcount_comfirm),



]
