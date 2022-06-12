from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def hello(request):
    return JsonResponse({'result':200,'msg':'Hello'})

'''

def register_view(request):
    if request.method != 'POST':
        return JsonResponse({'result':400,'msg':'登录仅支持POST方式'})
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    User.objects.create_user(username=username, password=password)
    user = authenticate(username=username, password=password)
    return JsonResponse({'result':200,'msg':'注册成功'})

'''

@csrf_exempt
def login_view(request):
    js = json.loads(request.body.decode('utf-8'))
    username = js.get('username',None)
    password = js.get('password',None)
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({'result':400,'msg':'用户名或密码错误'})

    return JsonResponse({'result':200,'msg':'登录成功'})