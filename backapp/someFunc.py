from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields,widgets
import json,re


def sum_allprice():
    order = models.order.objects.all()
    tb = models.table_manage.objects.all()
    fo = models.food_manage.objects.all()
    w = order.values('table_id')
    for i in w:
        q = i['table_id']
        co = models.food_choose.objects.filter(table_n=q).count()
        old_allprice = models.order.objects.filter(table_id=q).first().all_price
        if co > 1:
            u = models.food_choose.objects.filter(table_n=q).values('food_cho_id', 'food_count')
            # print(u)
            new_allprice = 0
            for i in u:
                food_cho_id = i['food_cho_id']
                food_count = i['food_count']
                print(food_count, food_cho_id)
                s = models.food_manage.objects.filter(id=food_cho_id).first().price
                new_allprice = new_allprice + int(s) * int(food_count)
                print(new_allprice)
            if new_allprice != old_allprice:
                models.order.objects.filter(table_id=q).update(all_price=new_allprice)
        elif co == 1:
            u = models.food_choose.objects.filter(table_n=q).values('food_cho_id','food_count')
            print(u[0]['food_cho_id'], u[0]['food_count'])
            food_cho_id = u[0]['food_cho_id']
            food_count = u[0]['food_count']
            s = models.food_manage.objects.filter(id=food_cho_id).first().price
            new_allprice = int(s) * int(food_count)
            print(new_allprice)
            if new_allprice != old_allprice:
                models.order.objects.filter(table_id=q).update(all_price=new_allprice)
        else:
            print('not any food_cho')
            models.order.objects.filter(table_id=q).update(all_price=0.00)
    # return render(request, 'back/order.html', {'order':order, 'tb':tb, 'fo':fo})