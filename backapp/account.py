from django.shortcuts import render,HttpResponse,redirect
from backapp import models
from django import forms
from django.forms import fields,widgets
import json,re


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
    username = fields.CharField(max_length=16,label='新用户名',
                                widget=forms.widgets.TextInput(attrs={'placeholder':'新用户名'}))
    password = fields.CharField(max_length=32,
                                widget=forms.widgets.PasswordInput(attrs={'placeholder':'密码'}),label='密码')
    email = fields.EmailField(max_length=32,
                              error_messages={'invalid':'邮箱格式错误'},
                               widget=widgets.TextInput(attrs={'placeholder':'邮箱'}))
    grouptype_id = fields.ChoiceField(
        choices=models.user_group.objects.values_list('id','groupname'),
    )
    def __init__(self, *args, **kwargs):
        super(user_infoForm,self).__init__(*args,**kwargs)
        self.fields['grouptype_id'].choices = models.user_group.objects.values_list('id','groupname')


#用户管理
@auth
def userinfo(request):
    if request.method == 'GET':
        obj = user_infoForm()
        # print(obj)
        user_list = models.user_info.objects.all()
        # for s in user_list:
        #     print(s.usame, s.grouptype.groupname)
        group_list = models.user_group.objects.all()
        # print(group_list.values_list('id','groupname'))
        return render(request, 'back/user_info.html', {'obj': obj, 'user_list': user_list,'group_list':group_list})
    elif request.method == 'POST':
        obj = user_infoForm(request.POST)
        # print(request.POST)
        result = obj.is_valid()
        er = obj.errors
        w = models.user_info.objects.filter(username=obj.cleaned_data['username']).first()
        # print('obj.cleaned_data: %s %s' % (obj.cleaned_data['username'], obj.cleaned_data.values()))
        if w:
            useradd_err = '创建失败, 用户' + obj.cleaned_data['username'] + '已存在'
        else:
            if result:
                models.user_info.objects.create(**obj.cleaned_data)
                useradd_err = '用户' + obj.cleaned_data['username'] + '创建成功'
            else:
                print(er)
                useradd_err = '输入的格式错误，创建失败'
        #models.user_info.objects.create(**{'username': 'gord015', 'password': '123456', 'email': 'aa@qq.cc', 'grouptype_id': '1'})
        obj = user_infoForm()
        # print(obj)
        user_list = models.user_info.objects.all()
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_info.html', {'obj': obj, 'user_list': user_list, 'group_list': group_list,'useradd_err':useradd_err})


#删除用户
# @auth
# def userdel(request,nid):
#     obj = user_infoForm()
#     user_list = models.user_info.objects.all()
#     group_list = models.user_group.objects.all()
#     u = request.session.get('username')
#     a = models.user_info.objects.filter(id=nid)
#     print(a)
#     for i in a:
#         s = i.username
#         print(s)
#     if s == u:
#         delerr = '删除失败! 不能删除正在登陆的用户: %s, 请退出登陆后由管理员帐户删除' %s
#     elif s == 'root':
#         delerr = '删除失败! 不能删除管理员帐户: root'
#     else:
#         w = models.user_info.objects.filter(id=nid).delete()
#         delerr = '用户: ' + s + '删除成功'
#     # return redirect('/back/user_info/')
#     return render(request, 'back/user_info.html',{'obj': obj,'user_list': user_list,'delerr': delerr,'group_list':group_list})

@auth
def userdel_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        i = request.POST.get('id')
        u = request.POST.get('username')
        s = request.session.get('username')
        # print(i,len(u),len(s),type(u))
        if u == s:
            ret['status'] = False
            ret['error'] = '删除失败! 不能删除正在登陆的用户: %s, 请退出登陆后由管理员帐户删除' %s
        elif u == 'root':
            ret['status'] = False
            ret['error'] = '删除失败! 不能删除管理员帐户: root'
        else:
            w = models.user_info.objects.filter(id=i).delete()  # 有id返回(1, {'backapp.table_manage': 1})，  无id返回(0, {'backapp.table_manage': 0})
            if w[0] == 1:
                # print(w)
                ret['error'] = '删除成功'
            else:
                ret['status'] = False
                ret['error'] = '删除失败'
    except Exception as e:
        # print(e)
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))


#编辑用户
@auth
def useredit_submit(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        # u = request.POST.get('user2')
        i = request.POST.get('edit_id2')
        p = request.POST.get('pwd2')
        e = request.POST.get('email2')
        g = request.POST.get('grouptype2')
        # print(i,u,p,e,g,type(g))
        es = models.user_info.objects.filter(id=i).values('email').first()
        # 判断邮箱格式是否正确(邮箱名称可以包含中文)
        if len(e) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", e) == None:
                ret['status'] = False
                ret['error'] = '邮箱格式错误'
        else:  # 邮箱长度1-7
            ret['status'] = False
            ret['error'] = '邮箱长度少于7位'
        if p and e:
            dic = {'password': p, 'email': e, 'grouptype': g}
        elif p:
            dic = {'password': p, 'grouptype': g}
        elif e:
            dic = {'email': e, 'grouptype': g}
        else:
            dic = {'grouptype': g}
        models.user_info.objects.filter(id=i).update(**dic)
        # # models.user_info.objects.filter(id=i).update(password=p,email=e,grouptype=g)
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))
    return HttpResponse(json.dumps(ret))



@auth
def useredit_ajax(request):
    ret = {'status': True, 'error': 'None', 'data': None}
    try:
        i = request.POST.get('id')
        # print(i)
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
    # print(type(ret))
    # print(ret)
    # print(json.dumps(ret))

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
        # print(g)
        if g:
            w = models.user_group.objects.filter(groupname=g).first()
            if w == None:
                models.user_group.objects.create(groupname=g)
                add_err = '用户组' + g + '添加成功'
            else:
                add_err = '用户组' + g + '已存在'
        else:
            add_err = '请输入新的用户组名称'
        group_list = models.user_group.objects.all()
        return render(request, 'back/user_group.html', {'group_list': group_list,'add_err': add_err})


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
    w = models.user_info.objects.all().filter(grouptype_id=nid).first()
    if w:
        groupdel_err = '删除失败，此用户组包含用户'
    else:
        groupdel_err = '此用户组删除成功'
        models.user_group.objects.all().filter(id=nid).delete()
    group_list = models.user_group.objects.all()
    return render(request, 'back/user_group.html', {'group_list': group_list, 'groupdel_err': groupdel_err})



