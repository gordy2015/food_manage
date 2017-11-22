from django.shortcuts import render,HttpResponse,redirect
from backapp import models,someFunc
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
        return render(request, 'back/table_manage.html',{'tm': tm})


@auth
def tableadd_ajax(request):
    ret = {'status': True, 'info': 'None', 'data': None}
    try:
        t = request.POST.get('tablename')
        if t.strip():  #判断输入的内容是否为空
            result = models.table_manage.objects.create(tablename=t)
            if result:
                ret['status'] = False
                ret['info'] = '添加成功'
            else:
                ret['status'] = False
                ret['info'] = '添加失败'
        else:
          ret['status'] = False
          ret['info'] = '添加失败，请输入桌名'
    except Exception as e:
        ret['status'] = False
        ret['info'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

@auth
def tableedit_ajax(request):
    ret = {'status': True, 'info': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.table_manage.objects.filter(id=i)
        if result:
            for s in result:
                ret['data'] = {'tablename': s.tablename}
        else:
            ret['status'] = False
            ret['info'] = 'not found this table'
    except Exception as e:
        ret['status'] = False
        ret['info'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


@auth
def tableedit_confirm(request):
    ret = {'status':True, 'info': None, 'data': None}
    try:
        i = request.POST.get('tid')
        t = request.POST.get('tablename')
        # print(i,t,o,s)
        if t:
            models.table_manage.objects.filter(id=i).update(tablename=t)
        else:
            ret['status'] = False
            ret['info'] = '请输入完整的数据'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    return HttpResponse(json.dumps(ret))


@auth
def tabledel_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        p = models.order.objects.filter(table_id=i).count()
        if p <= 0:
            w = models.table_manage.objects.filter(id=i).delete() #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
            if w[0] == 1:
                ret['info'] = '删除成功'
                # print(w[0])
            else:
                ret['status'] = False
                ret['info'] = '删除失败'
        else:
            ret['status'] = False
            ret['info'] = '不能删除，存在此餐桌的订单'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    return HttpResponse(json.dumps(ret))

#菜系管理
@auth
def foodtype_manage(request):
    foodtype = models.foodtype_manage.objects.all()
    # print(foodtype.values('foodtypename'))
    return render(request, 'back/foodtype_manage.html',{'foodtype':foodtype})

@auth
def foodtype_add_ajax(request):
    ret = {'status':True, 'info':None, 'data':None}
    try:
        f = request.POST.get('foodtypename')
        if f:
            w = models.foodtype_manage.objects.create(foodtypename=f)
            if w:
                ret['info'] = '添加成功'
            else:
                ret['status'] = False
                ret['info'] = '添加失败'
        else:
            ret['status'] = False
            ret['info'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))

@auth
def foodtypeedit_ajax(request):
    ret = {'status': True, 'info': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.foodtype_manage.objects.filter(id=i)
        if result:
            for s in result:
                ret['data'] = {'foodtypename': s.foodtypename}
        else:
            ret['status'] = False
            ret['info'] = 'not found this foodtypename'
    except Exception as e:
        ret['status'] = False
        ret['info'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

@auth
def foodtypeedit_confirm(request):
    ret = {'status':True, 'info':None, 'data':None}
    try:
        i = request.POST.get('tid')
        f = request.POST.get('foodtypename')
        if f:
            w = models.foodtype_manage.objects.filter(id=i).update(foodtypename=f)
            if w:
                ret['info'] = '修改成功'
            else:
                ret['status'] = False
                ret['info'] = '修改失败'
        else:
            ret['status'] = False
            ret['info'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    # print(ret)
    return HttpResponse(json.dumps(ret))


@auth
def foodtype_del_ajax(request):
    ret = {'status':True, 'info':None, 'data':None}
    try:
        i = request.POST.get('id')
        if i:
            s = models.food_manage.objects.filter(foodtype_id=i).count()
            if s <= 0:
                w = models.foodtype_manage.objects.filter(id=i).delete()
                if w:
                    ret['info'] = '删除成功'
                else:
                    ret['status'] = False
                    ret['info'] = '删除失败'
            else:
                ret['status'] = False
                ret['info'] = '不能删除，此菜系下有菜品'
        else:
            ret['status'] = False
            ret['info'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
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
    ret = {'status':True, 'info':None, 'data':None}
    try:
        f = request.POST.get('foodname')
        p = request.POST.get('price')
        v = request.POST.get('vip_price')
        t = request.POST.get('foodtypename')
        if f and p and v and t:
            fo = {'foodname':f,'price':p,'vip_price':v,'foodtype_id':t}
            w = models.food_manage.objects.create(**fo)  #有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
            if w:
                ret['info'] = '添加成功'
            else:
                ret['status'] = False
                ret['info'] = '添加失败'
        else:
            ret['status'] = False
            ret['info'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    return HttpResponse(json.dumps(ret))



@auth
def foodedit_ajax(request):
    ret = {'status': True, 'info': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        result = models.food_manage.objects.filter(id=i)
        if result:
            for s in result:  #价格的数据类型使用了DecimalField，会返回Float类型 导致json.dumps(ret)会报错 TypeError: Object of type 'Decimal' is not JSON serializable， 所以转成str(s.price)和str(s.vip_price)
                ret['data'] = {'foodname': s.foodname, 'price': str(s.price), 'vip_price': str(s.vip_price), 'foodtype_id': s.foodtype_id}
        else:
            ret['status'] = False
            ret['info'] = 'not found this food'
    except Exception as e:
        ret['status'] = False
        ret['info'] = 'request error'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

@auth
def foodedit_confirm(request):
    ret = {'status': True, 'info': None, 'data': None}
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
                ret['info'] = '修改成功'
            else:
                ret['status'] = False
                ret['info'] = '修改失败'
        else:
            ret['status'] = False
            ret['info'] = '内容不能为空'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    return HttpResponse(json.dumps(ret))

@auth
def food_del_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        p = models.food_choose.objects.filter(food_cho_id=i).count()
        if p <= 0:
            w = models.food_manage.objects.all().filter(id=i).delete()
            if w[0] == 1:
                ret['info'] = '删除成功'
            else:
                ret['status'] = False
                ret['info'] = '删除失败'
        else:
            ret['status'] = False
            ret['info'] = '不能删除，此菜品存在订单中'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
    return HttpResponse(json.dumps(ret))


# 餐厅订单&总价计算
@auth
def order(request):
    order = models.order.objects.all()
    tb = models.table_manage.objects.all()
    fo = models.food_manage.objects.all()
    someFunc.sum_allprice()
    return render(request, 'back/order.html', {'order':order, 'tb':tb, 'fo':fo})


#点餐（需要判断之前有无此订单，有要判断之前有无已点过同样的菜品，如果点过，要在原菜品所点的数量上进行增加，没点过直接添加新的菜品，并将菜品与订单做关联。 如果没点过这个订单，要创建新的订单和新的菜品，并把它们关联起来（order_detail））
@auth
def order_add_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        t = request.POST.get('tablename_id')
        f = request.POST.get('food_cho_id')
        fcount = request.POST.get('food_count')
        v = request.POST.get('viptype')
        o = request.POST.get('orderstatus')
        if int(fcount):
            ou_id = someFunc.randomnum()
            nod = {'table_id':t, 'orderstatus':o, 'vip_type':v, 'ou_id':ou_id}
            cnod = models.order.objects.create(**nod)
            if cnod:
                order_id = models.order.objects.filter(ou_id=ou_id).first().id
                nfc = {'food_cho_id':f, 'food_count':fcount, 'ou_id':ou_id, 'order_n_id':order_id}
                cnfc = models.food_choose.objects.create(**nfc)
                # # print(t,f,fcount,v,o)
                # # print('nod:%s, nfc:%s, nod_id:%s' %(nod,nfc,nod_id))
                if cnfc:
                    ret['status'] = True
                    ret['info'] = '添加成功'
                else:
                    ret['status'] = False
                    ret['info'] = '添加失败'
        else:
            ret['status'] = False
            ret['info'] = '添加失败'
    except ValueError as e:
        ret['status'] = False
        ret['info'] = '数量栏请输入数字'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))

@auth
def order_del_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        m = models.order.objects.filter(id=i).delete()
        fd = models.food_choose.objects.filter(order_n=i).delete()
        if m and fd:
            ret['status'] = True
            ret['info'] = '删除成功'
        else:
            ret['status'] = False
            ret['info'] = '删除失败'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))

@auth
def order_edit_comfirm(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        ntn = request.POST.get('ntn')
        ntime = request.POST.get('ntime')
        nvt = request.POST.get('nvt')
        nos = request.POST.get('nos')
        if ntn and ntime and nvt and nos:
            order_edit_dic = {'table_id':ntn, 'ordertime':ntime, 'vip_type':nvt, 'orderstatus':nos}
            m = models.order.objects.filter(id=i).update(**order_edit_dic)
            if m:
                ret['status'] = True
                ret['info'] = '订单修改成功'
            else:
                ret['status'] = False
                ret['info'] = '订单修改失败'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))


@auth
def order_pay_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        m = models.order.objects.filter(id=i).first().orderstatus
        if m == 1:
            ret['status'] = False
            ret['info'] = '此订单已结算，无需再次结算'
        else:
            tm = models.order.objects.filter(id=i).update(orderstatus=1)
            if tm:
                ret['status'] = True
                ret['info'] = '订单结算成功'
            else:
                ret['status'] = False
                ret['info'] = '订单结算失败'

    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))


@auth
def order_detail(request,nid):
    fo = models.food_manage.objects.all()
    fc = models.food_choose.objects.filter(order_n_id=nid)
    # for i in od:
    #     print(i.order_n.vip_type)
    if fc:
        someFunc.sum_allprice()
        all_price = fc.first().order_n.all_price
    else:
        all_price = 0.00
    return render(request,'back/order_detail.html',{'fc':fc, 'all_price':all_price, 'fo':fo})

@auth #删除单个菜品
def fc_del_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        fd = models.food_choose.objects.filter(id=i).delete()
        if fd:
            ret['status'] = True
            ret['info'] = '删除成功'
        else:
            ret['status'] = False
            ret['info'] = '删除失败'

    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))

def fcount_comfirm(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        c = request.POST.get('nfcount')
        if int(c):
            p = models.food_choose.objects.filter(id=i).first().food_count
            if c != p:
                q = models.food_choose.objects.filter(id=i).update(food_count=c)
                if q:
                    ret['status'] = True
                    ret['info'] = '修改成功'
                else:
                    ret['status'] = False
                    ret['info'] = '修改失败'
    except ValueError as e:
        ret['status'] = False
        ret['info'] = '数量栏请输入数字'

    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误或请输入数字'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))

def fc_add_ajax(request):
    ret = {'status': True, 'info': None, 'data': None}
    try:
        i = request.POST.get('id')
        f = request.POST.get('new_food_cho_id')
        fcount = request.POST.get('new_food_count')
        if int(fcount):
            ouid = models.food_choose.objects.filter(id=i).first().ou_id
            order_nid = models.food_choose.objects.filter(id=i).first().order_n_id
            query_fc = {'food_cho_id': f, 'ou_id': ouid, 'order_n_id': order_nid}
            q = models.food_choose.objects.filter(**query_fc)
            p = None
            if q:  #如果所选的菜品已存在，则在原数量的基础上增加上新的数量
                old_fcount = models.food_choose.objects.filter(**query_fc)
                if old_fcount:
                    new_fcount = int(fcount) + old_fcount.first().food_count
                    # print(old_fcount.first().food_count, int(fcount), type(fcount), new_fcount)
                    p = models.food_choose.objects.filter(**query_fc).update(food_count=new_fcount)
            else:
                new_fc = {'food_count':fcount, 'food_cho_id':f, 'ou_id':ouid, 'order_n_id':order_nid}
                p = models.food_choose.objects.create(**new_fc)
            if p:
                ret['status'] = True
                ret['info'] = '添加成功'
            else:
                ret['status'] = False
                ret['info'] = '添加失败'
    except ValueError as e:
        ret['status'] = False
        ret['info'] = '数量栏请输入数字'
    except Exception as e:
        ret['status'] = False
        ret['info'] = '请求错误'
        print('EXCEPTION:%s' % e)
    return HttpResponse(json.dumps(ret))


