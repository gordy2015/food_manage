from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields
import json



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

@auth
def tableedit_ajax(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.table_manage.objects.filter(id=i)
        if result:
            for s in result:
                ret['data'] = {'tablename': s.tablename, 'ts_id': s.ts_id, 'ordertime': s.ordertime}
        else:
            ret['status'] = False
            ret['error'] = 'not found this table'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


@auth
def tableedit_confirm(request):
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
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))


@auth
def table_del_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('id')
        w = models.table_manage.objects.filter(id=i).delete() #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
        if w[0] == 1:
            ret['error'] = '删除成功'
            # print(w[0])
        else:
            ret['status'] = False
            ret['error'] = '删除失败'
    except Exception as e:
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
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))

@auth
def foodtypeedit_ajax(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.foodtype_manage.objects.filter(id=i)
        if result:
            for s in result:
                ret['data'] = {'foodtypename': s.foodtypename}
        else:
            ret['status'] = False
            ret['error'] = 'not found this foodtypename'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

@auth
def foodtypeedit_confirm(request):
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
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))

@auth
def foodtype_del_ajax(request):
    ret = {'status':True, 'error':None, 'data':None}
    try:
        i = request.POST.get('id')
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
        ret['status'] = False
        ret['error'] = '请求错误'
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
            w = models.food_manage.objects.create(**fo)  #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
            if w:
                ret['error'] = '添加成功'
            else:
                ret['status'] = False
                ret['error'] = '添加失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))



@auth
def foodedit_ajax(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.food_manage.objects.filter(id=i)
        if result:
            for s in result:  #价格的数据类型使用了DecimalField，会返回Float类型 导致json.dumps(ret)会报错 TypeError: Object of type 'Decimal' is not JSON serializable， 所以转成str(s.price)和str(s.vip_price)
                ret['data'] = {'foodname': s.foodname, 'price': str(s.price), 'vip_price': str(s.vip_price), 'foodtype_id': s.foodtype_id}
        else:
            ret['status'] = False
            ret['error'] = 'not found this food'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

@auth
def foodedit_confirm(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('tid')
        f = request.POST.get('foodname')
        p = request.POST.get('price')
        v = request.POST.get('vip_price')
        ft = request.POST.get('foodtypename')
        # print('i:%s  f:%s  p:%s  v:%s  ft:%s' %(i,f,p,v,ft))
        if f and p and v and ft:
            fo = {'foodname': f, 'price': p, 'vip_price': v, 'foodtype_id': ft}
            w = models.food_manage.objects.all().filter(id=i).update(**fo)
            if w:
                ret['error'] = '修改成功'
            else:
                ret['status'] = False
                ret['error'] = '修改失败'
        else:
            ret['status'] = False
            ret['error'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))

@auth
def food_del_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('id')
        w = models.food_manage.objects.all().filter(id=i).delete()
        if w[0] == 1:
            ret['error'] = '删除成功'
        else:
            ret['status'] = False
            ret['error'] = '删除失败'
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))


# 餐厅订单
@auth
def order(request):
    order = models.order.objects.all()
    tb = models.table_manage.objects.all()
    fo = models.food_manage.objects.all()
    return render(request, 'back/order.html', {'order':order, 'tb':tb, 'fo':fo})


@auth
def order_add_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        t = request.POST.get('tablename_id')
        f = request.POST.get('food_cho_id')
        fc = request.POST.get('food_count')
        print(t, f, fc)
        w = models.order.objects.filter(table_id=t)
        if w: #order存在
            od_id = w.first().id
            print('order %s is exist' %t)
            # oi = models.order.objects.filter(table_id=t).first().id
            tn = models.food_choose.objects.filter(table_n=t,food_cho_id=f).first()
            # fc_id = None
            if tn:  #order和food_cho_id都存在
                print('food_cho_id %s is exist' %f)
                print(tn.food_count)
                fc_id = None
                new_fc_count = int(tn.food_count) + int(fc)
                nf = {'food_cho_id': f, 'food_count': tn.food_count, 'table_n': t}
                models.food_choose.objects.filter(**nf).update(food_count=str(new_fc_count))
                # fc_id = models.food_choose.objects.filter(food_cho_id=f, table_n=t, food_count=str(new_fc_count))

            else: #order存在，但food_cho_id不存在
                print('food_cho_id %s is not exist' %f)
                nf = {'food_cho_id':f, 'food_count':fc, 'table_n':t}
                models.food_choose.objects.create(**nf)
                fc_id = models.food_choose.objects.filter(**nf).first().id


        else: #order不存在
            print('order %s is not exist')
            #添加这个新的order
            models.order.objects.create(table_id=t)
            od_id = models.order.objects.filter(table_id=t).first().id
            print('food_cho_id %s is not exist' % f)
            nf = {'food_cho_id': f, 'food_count': fc, 'table_n': t}
            models.food_choose.objects.create(**nf)
            fc_id = models.food_choose.objects.filter(**nf).first().id
        if fc_id:
            od_dict = {'thisorder_id':od_id, 'thisfc_id':fc_id}
            q = models.order_detail.objects.filter(**od_dict)
            if q:
                print('order_detail %s is exist' %q.first().id)
            else:
                print('order_detail is not exist')
                models.order_detail.objects.create(**od_dict)


    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))

@auth
def order_detail(request,nid):
    od = models.order_detail.objects.filter(thisorder_id=nid)
    # print(od)
    # for i in od:
    #     print(i.id,i.thisfc.food_cho.foodname)
    return render(request,'back/order_detail.html',{'od':od})