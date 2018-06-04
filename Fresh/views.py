from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from Fresh import models
# 首页
def index(request):
    return render(request,'Fresh/index.html')


def register(request):
    return render(request,'Fresh/register.html')
def user_isregister(request):
    username = request.GET.get('username')
    ret = models.User.objects.filter(username=username)
    msg = {'status':0,'msg':''}
    if ret:
        msg['status'] = 1
        msg['msg'] = '用户名已存在'

    return JsonResponse(msg)
def ajax_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = {'status': 0, 'msg': ''}
        try:
            user_obj = models.User.objects.create(username=username,password=password)
            user_info_obj = models.UserInfo.objects.create(phone=phone,email=email,user=user_obj)
            msg['msg'] = '/index/'
        except Exception :
            msg['status'] = 1
            msg['msg'] = '注册失败'

        return JsonResponse(msg)
    return HttpResponse('ok')