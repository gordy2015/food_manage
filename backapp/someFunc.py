from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields,widgets
import json,re

#for v0.1
def sum_allprice_oldver01():
    order = models.order.objects.all()
    tb = models.table_manage.objects.all()
    fo = models.food_manage.objects.all()
    w = order.values('table_id')
    for i in w:
        q = i['table_id']
        co = models.food_choose.objects.filter(table_n=q).count()
        old_allprice = models.order.objects.filter(table_id=q).first().all_price
        tt = models.order.objects.filter(table_id=q).first().table.tlevel_type
        if co > 1:
            u = models.food_choose.objects.filter(table_n=q).values('food_cho_id', 'food_count')
            # print(u)
            new_allprice = 0
            for i in u:
                food_cho_id = i['food_cho_id']
                food_count = i['food_count']
                if tt == 0:
                    s = models.food_manage.objects.filter(id=food_cho_id).first().price
                else:
                    s = models.food_manage.objects.filter(id=food_cho_id).first().vip_price
                new_allprice = new_allprice + int(s) * int(food_count)
            if new_allprice != old_allprice:
                models.order.objects.filter(table_id=q).update(all_price=new_allprice)
        elif co == 1:
            u = models.food_choose.objects.filter(table_n=q).values('food_cho_id','food_count')
            # print(u[0]['food_cho_id'], u[0]['food_count'])
            food_cho_id = u[0]['food_cho_id']
            food_count = u[0]['food_count']
            if tt == 0:
                s = models.food_manage.objects.filter(id=food_cho_id).first().price
            else:
                s = models.food_manage.objects.filter(id=food_cho_id).first().vip_price
            new_allprice = int(s) * int(food_count)
            if new_allprice != old_allprice:
                models.order.objects.filter(table_id=q).update(all_price=new_allprice)
        else:
            print('not any food_cho')
            models.order.objects.filter(table_id=q).update(all_price=0.00)
    # return render(request, 'back/order.html', {'order':order, 'tb':tb, 'fo':fo})


#for v0.2
def sum_allprice():
    order = models.order.objects.all()
    oder_status = order.first().orderstatus
    fc = models.food_choose.objects.all()
    w = order.values('id')
    print(w)
    for i in w:
        # print(i['id'])
        order_id = i['id']
        q = models.food_choose.objects.filter(order_n_id=i['id'])
        old_allprice = models.order.objects.filter(id=order_id).first().all_price
        co = models.food_choose.objects.filter(order_n_id=i['id']).count()
        print(co)
        if co > 1:
            u = models.food_choose.objects.filter(order_n_id=order_id).values('food_cho_id', 'food_count')
            # print(u)
            new_allprice = 0
            for i in u:
                food_cho_id = i['food_cho_id']
                food_count = i['food_count']
                if oder_status == 0:
                    s = models.food_manage.objects.filter(id=food_cho_id).first().price
                else:
                    s = models.food_manage.objects.filter(id=food_cho_id).first().vip_price
                new_allprice = new_allprice + int(s) * int(food_count)
                print('new_allprice: %s %s' %(type(new_allprice), new_allprice))
            if new_allprice != old_allprice:
                models.order.objects.filter(id=order_id).update(all_price=new_allprice)
        elif co == 1:
            u = models.food_choose.objects.filter(order_n_id=order_id).values('food_cho_id', 'food_count')
            food_cho_id = u[0]['food_cho_id']
            food_count = u[0]['food_count']
            if oder_status == 0:
                s = models.food_manage.objects.filter(id=food_cho_id).first().price
            else:
                s = models.food_manage.objects.filter(id=food_cho_id).first().vip_price
            new_allprice = int(s) * int(food_count)
            # print('here: %s %s %s' % (food_cho_id, food_count, new_allprice))
            if new_allprice != old_allprice:
                models.order.objects.filter(id=order_id).update(all_price=new_allprice)
        elif co == 0:
            models.order.objects.filter(id=order_id).update(all_price=0.00)




