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


#主页/登陆页
def index(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        l = request.POST.get('login7days')
        print(u,p ,l )
        w = models.user_info.objects.filter(username=u,password=p)
        if w:
            request.session['username'] = u
            request.session['is_login'] = True
            if l:
                request.session.set_expiry(604800)
            else:
                request.session.set_expiry(86400)
            return redirect('/back/user_info/')
        else:
            return redirect('/back/index/')
    elif request.method == 'GET':
        v = request.session.get('is_login')
        if v:
            return redirect('/back/user_info/')
        else:
            return render(request, 'back/index.html')

#退出
def logout(request):
    request.session.clear()
    return redirect('/back/index/')


class user_infoForm(forms.Form):
    username = fields.CharField(max_length=16)
    password = fields.CharField(max_length=32)
    email = fields.EmailField(max_length=32)
    grouptype = fields.ChoiceField(
        choices=models.user_group.objects.values_list('id','groupname')
    )


@auth
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
@auth
def user_group(request):
    return render(request, 'back/user_group.html')


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

