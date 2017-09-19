from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields




#登陆检测装饰器
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.session.get('is_login')
        if not v:
            return redirect('/back/index/')
        return func(request, *args, **kwargs)
    return inner


#餐桌管理
@auth
def table_manage(request):
    tm = models.table_manage.objects.all()
    tst = models.table_status.objects.all()
    return render(request, 'back/table_manage.html',{'tm': tm, 'tst': tst})


#菜系管理
@auth
def foodtype_manage(request):
    return render(request, 'back/foodtype_manage.html')


#菜品管理
@auth
def food_manage(request):
    return render(request, 'back/food_manage.html')


# 餐厅订单
@auth
def restaurant_order(request):
    return render(request, 'back/restaurant_order.html')

