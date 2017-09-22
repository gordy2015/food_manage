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
    if request.method == 'GET':
        tm = models.table_manage.objects.all()
        tst = models.table_status.objects.all()
        return render(request, 'back/table_manage.html',{'tm': tm, 'tst': tst})
    elif request.method == 'POST':
        t = request.POST.get('tablename')
        o = request.POST.get('ordertime')
        s = request.POST.get('tablestatus')
        if t and o:
            models.table_manage.objects.create(tablename=t,ordertime=o,ts_id=s)
        return redirect('/back/table_manage/')
import json
@auth
def table_edit_ajax(request):
    ret = {'status':True, 'error': None, 'data': None}
    try:
        i = request.POST.get('tid')
        t = request.POST.get('tablename')
        o = request.POST.get('ordertime')
        s = request.POST.get('tablestatus')
        print(i,t,o,s)
        if t and o and s:
            dic = {'tablename':t, 'ordertime':o, 'ts_id':s}
            models.table_manage.objects.filter(id=i).update(**dic)
        else:
            ret['status'] = False
            ret['error'] = '请输入完整的数据'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))


@auth
def table_del_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('id')
        print(i)
        w = models.table_manage.objects.filter(id=i).delete() #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
        if w[0] == 1:
            ret['error'] = '删除成功'
            # print(w[0])
        else:
            ret['status'] = False
            ret['error'] = '删除失败'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))

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

