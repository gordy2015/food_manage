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
        # print(i,t,o,s)
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
    foodtype = models.foodtype_manage.objects.all()
    # print(foodtype.values('foodtypename'))
    return render(request, 'back/foodtype_manage.html',{'foodtype':foodtype})

@auth
def foodtype_add_ajax(request):
    ret = {'status':True, 'error':None, 'data':None}
    try:
        f = request.POST.get('foodtypename')
        if f:
            w = models.foodtype_manage.objects.create(foodtypename=f)
            if w:
                ret['error'] = '添加成功'
            else:
                ret['status'] = False
                ret['error'] = '添加失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))



@auth
def foodtype_edit_ajax(request):
    ret = {'status':True, 'error':None, 'data':None}
    try:
        i = request.POST.get('tid')
        f = request.POST.get('foodtypename')
        if f:
            w = models.foodtype_manage.objects.filter(id=i).update(foodtypename=f)
            if w:
                ret['error'] = '修改成功'
            else:
                ret['status'] = False
                ret['error'] = '修改失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))

@auth
def foodtype_del_ajax(request):
    ret = {'status':True, 'error':None, 'data':None}
    try:
        i = request.POST.get('id')
        print(i)
        if i:
            w = models.foodtype_manage.objects.filter(id=i).delete()
            if w:
                ret['error'] = '删除成功'
            else:
                ret['status'] = False
                ret['error'] = '删除失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    print(ret)
    return HttpResponse(json.dumps(ret))



#菜品管理
@auth
def food_manage(request):
    food = models.food_manage.objects.all()
    foodtype = models.foodtype_manage.objects.all()
    return render(request, 'back/food_manage.html',{'food':food,'foodtype':foodtype})

#添加菜品
@auth
def food_add_ajax(request):
    ret = {'status':True, 'error':None, 'data':None}
    try:
        f = request.POST.get('foodname')
        p = request.POST.get('price')
        v = request.POST.get('vip_price')
        t = request.POST.get('foodtypename')
        if f and p and v and t:
            fo = {'foodname':f,'price':p,'vip_price':v,'foodtype_id':t}
            print(fo)
            w = models.food_manage.objects.create(**fo) #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
            if w:
                ret['error'] = '添加成功'
            else:
                ret['status'] = False
                ret['error'] = '添加失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))

@auth
def food_del_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('id')
        print(i)
        w = models.food_manage.objects.all().filter(id=i).delete()
        if w[0] == 1:
            ret['error'] = '删除成功'
        else:
            ret['status'] = False
            ret['error'] = '删除失败'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    print(ret)
    return HttpResponse(json.dumps(ret))


# 餐厅订单
@auth
def restaurant_order(request):
    order = models.order.objects.all()
    table = models.table_manage.objects.all()
    od = models.order_detail.objects.all()
    # print(order.values('all_price'))
    fo = models.food_manage.objects.all()

    # for s in od:
    #     print(s.food_cho.foodname,s.food_count)


    # for m in od:
    #     # print(m.order_d.id)
    #     for s in m.order_d.all():
    #         print(s.all_price,s.orderstatus,s.tablename.tablename,s.tablename.ordertime)
    return render(request, 'back/restaurant_order.html',{'order':order,'table':table,'od':od,'fo':fo})


@auth
def order_add_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        t = request.POST.get('tablename')
        f = request.POST.get('food_cho')
        fc = request.POST.get('food_count')
        s = request.POST.get('status')
        print(t,f, fc, s)
        if t:
            fo = {'food_cho_id': f, 'food_count': fc}
            models.order_detail.objects.create(**fo)
            q = models.order.objects.all().filter(tablename_id=t).values('id').first()
            print('result: %s %s' % (type(q), q['id']))
            if q:
                new_fc = models.order.objects.get(id=q['id'])
                order_detaild = models.order_detail.objects.all()
                print('n:%s , nd: %s' %(new_fc, order_detaild))
                order_detaild.order_d.add(new_fc)
                # w = new_order.order_d.add(**new_order)
                # if w:
                #     ret['error'] = '添加成功'
                # else:
                #     ret['status'] = False
                #     ret['error'] = '添加失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'

    except Exception as e:
        print('e:%s' %e)
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))

