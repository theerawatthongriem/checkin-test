from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Events
from django.contrib.auth.decorators import login_required
from .forms import EventsForm

def sign_in(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.error(request, 'เข้าสู่ระบบเรียบร้อย')
            return redirect('events') 
        elif user is not None and user.is_active:
            messages.error(request, 'คุณไม่ได้รับอนุญาตให้เข้าถึง')
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    return render(request,'officers/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='sign_in')
def events(request):
    event = Events.objects.filter(user=request.user)
    return render(request,'officers/events.html',{
        'event':event,
    })


@login_required(login_url='sign_in')
def add_event(request):
    form = EventsForm()
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = EventsForm(request.POST,request.FILES)
    
    return render(request,'officers/add_event.html',{
        'form':form
    })