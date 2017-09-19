from django.shortcuts import render

# Create your views here.


# 定义网站首页http://127.0.0.1:8000/
def index(request):
    return render(request, 'front/index.html')


