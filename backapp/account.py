from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields,widgets


#登陆检测装饰器
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.session.get('is_login')
        if not v:
            return redirect('/back/index/')
        return func(request, *args, **kwargs)
    return inner


#主页/登陆首页
def index(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        l = request.POST.get('login7days')
        # print(u,p ,l )
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
            loginerr = '用户名或密码错误，请重试'
            # return redirect('/back/index/')
            return render(request, 'back/index.html',{'loginerr':loginerr})
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
    password = fields.CharField(max_length=32,
                                widget=forms.widgets.PasswordInput)
    email = fields.EmailField(max_length=32)
    grouptype_id = fields.ChoiceField(
        choices=models.user_group.objects.values_list('id','groupname')
    )
    # def __init__(self, *args, **kwargs):
    #     super(user_infoForm,self).__init__(*args,**kwargs)
    #     self.fields['grouptype'].choices = models.user_group.objects.values_list('id','groupname')


#用户管理
@auth
def userinfo(request):
    if request.method == 'GET':
        obj = user_infoForm()
        user_list = models.user_info.objects.all()
        # for s in user_list:
        #     print(s.username, s.grouptype.groupname)
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_info.html', {'obj': obj, 'user_list': user_list,'group_list':group_list})
    elif request.method == 'POST':
        obj = user_infoForm(request.POST)
        print(request.POST)
        obj.is_valid()
        obj.errors
        print(obj.cleaned_data)
        models.user_info.objects.create(**obj.cleaned_data)
        #models.user_info.objects.create(**{'username': 'gord015', 'password': '123456', 'email': 'aa@qq.cc', 'grouptype_id': '1'})
        return redirect('/back/user_info/')


#删除用户
@auth
def userdel(request,nid):
    obj = user_infoForm()
    user_list = models.user_info.objects.all()
    u = request.session.get('username')
    a = models.user_info.objects.filter(id=nid)
    print(a)
    for i in a:
        s = i.username
        print(s)
    if s == u:
        delerr = '删除失败! 不能删除正在登陆的用户: %s, 请退出登陆后由管理员帐户删除' %s
    elif s == 'root':
        delerr = '删除失败! 不能删除管理员帐户: root'
    else:
        w = models.user_info.objects.filter(id=nid).delete()
        delerr = '用户: ' + s + '删除成功'
    # return redirect('/back/user_info/')
    return render(request, 'back/user_info.html',{'obj': obj,'user_list': user_list,'delerr': delerr})

#编辑用户
@auth
def useredit(request):
    if request.method == 'POST':
        i = request.POST.get('edit_id2')
        u = request.POST.get('user2')
        p = request.POST.get('pwd2')
        e = request.POST.get('email2')
        g = request.POST.get('grouptype2')
        # print(i,u,p,e,g,type(g))
        if p:
            dic = {'password':p,'email':e,'grouptype':g}
        else:
            dic = {'email':e,'grouptype':g}
        #models.user_info.objects.filter(id=i).update(password=p,email=e,grouptype=g)
        models.user_info.objects.filter(id=i).update(**dic)
        return redirect('/back/user_info/')

import json
@auth
def useredit_ajax(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        print(i)
        result = models.user_info.objects.filter(id=i)
        # print(result)
        for s in result:
            # print(s)
            m = {'email':s.email, 'grouptype': s.grouptype_id}
        if result:
            ret['data'] = m

        else:
            ret['status'] = False
            ret['error'] = 'not found this user'
    except Exception as e:
        ret['status'] = False
        ret['error'] = 'request error'
    print(type(ret))
    print(ret)
    print(json.dumps(ret))

    return HttpResponse(json.dumps(ret))


#用户详情
@auth
def userdetail(request,nid):
    obj = user_infoForm()
    user_list= models.user_info.objects.all()
    group_list = models.user_group.objects.all()
    user_detail = models.user_info.objects.all().filter(id=nid)
    return render(request, 'back/user_info.html', {'obj': obj, 'user_list': user_list, 'user_detail': user_detail,'group_list':group_list})



#用户组管理
@auth
def groupinfo(request):
    if request.method == 'GET':
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_group.html', {'group_list':group_list})
    elif request.method == 'POST':
        g = request.POST.get('groupname')
        print(g)
        if g:
            models.user_group.objects.create(groupname=g)
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_group.html', {'group_list': group_list})


#用户组详细
@auth
def groupdetail(request,nid):
    group_list = models.user_group.objects.all()
    return render(request, 'back/user_group.html', {'group_list': group_list})


#用户组编辑
@auth
def groupedit(request):
    if request.method == 'GET':
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_group.html', {'group_list': group_list})
    elif request.method == 'POST':
        i = request.POST.get('gid')
        g = request.POST.get('groupname')
        if g:
            models.user_group.objects.all().filter(id=i).update(groupname=g)
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_group.html', {'group_list': group_list})


#用户组删除
@auth
def groupdel(request,nid):
    models.user_group.objects.all().filter(id=nid).delete()
    group_list = models.user_group.objects.all()
    return render(request, 'back/user_group.html', {'group_list': group_list})



