from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from officers.models import Events

def index(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and not user.is_staff:
            login(request, user)
            messages.error(request, 'เข้าสู่ระบบเรียบร้อย')
            return redirect('list') 
        elif user is not None and user.is_staff:
            messages.error(request, 'คุณไม่ได้รับอนุญาตให้เข้าถึง')
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    return render(request,'index.html')

def list_events(request):
    event = Events.objects.all()
    return render(request,'mainapp/list.html',{
        'event':event
    })

def event_detail(request,id):
    event = Events.objects.get(pk=id)
    return render(request,'mainapp/event_detail.html',{
        'event':event
    })