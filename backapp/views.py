from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields



#主页
def index(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        w = models.user_info.objects.filter(username=u,password=p)
        if w:
            return redirect('/back/user_info/')
        else:
            return redirect('/back/index/')
    elif request.method == 'GET':
        return render(request, 'back/index.html')



#用户管理
class user_infoForm(forms.Form):
    username = fields.CharField(max_length=16)
    password = fields.CharField(max_length=32)
    email = fields.EmailField(max_length=32)
    grouptype = fields.ChoiceField(
        choices=models.user_group.objects.values_list('id','groupname')
    )

def user_info(request):
    if request.method == 'POST':
        obj = user_infoForm(request.POST)
        obj.is_valid()
        obj.errors
        return render(request, 'back/user_info.html',{'obj':obj})
    elif request.method == 'GET':
        obj = user_infoForm()
        return render(request, 'back/user_info.html', {'obj':obj})


#用户组管理
def user_group(request):
    return render(request, 'back/user_group.html')


#餐桌管理
def table_manage(request):
    tm = models.table_manage.objects.all()
    tst = models.table_status.objects.all()
    return render(request, 'back/table_manage.html',{'tm': tm, 'tst': tst})


#菜系管理
def foodtype_manage(request):
    return render(request, 'back/foodtype_manage.html')


#菜品管理
def food_manage(request):
    return render(request, 'back/food_manage.html')


# 餐厅订单
def restaurant_order(request):
    return render(request, 'back/restaurant_order.html')

