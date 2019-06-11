from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Cs
from .models import Fs
from .models import Os
from .models import Dong
from .models import Childuser
from .models import Parentuser

# Create your views here.
def home(request):
    childUser = Childuser.objects
    parentUser = Parentuser.objects
    return render(request, 'home.html', {'childUser': childUser , 'parentUser' : parentUser})


def select(request):
    return render(request, 'select.html')

def select2(request):
    return render(request, 'select2.html')


def loginChild(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['PW']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginChild.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'loginChild.html')


def loginParent(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['PW']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginParent.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'loginParent.html')

def childSignup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['childID'], password=request.POST['childPW'])
        auth.login(request, user)
        myusers = Childuser()
        myusers.UserName = request.POST.get('childName','')
        myusers.UserID = request.POST.get('childID','')
        myusers.UserPW = request.POST.get('childPW','')
        myusers.UserFlag = "Child"
        myusers.save()
        return redirect('home')
    return render(request, 'childSignup.html')

def parentSignup(request):
    if request.method == 'POST':
        cnt =0
        

        for i in Childuser.objects.all() :
            if(i.UserName == request.POST.get('childName','')):
                cnt=1

        if(cnt==0):
            return render(request, 'parentSignup.html', {'error': '아이를 먼저 등록하세요'})
        
        else:
            user = User.objects.create_user(request.POST['parentID'], password=request.POST['parentPW'])
            auth.login(request, user)
            myusers = Parentuser()
            myusers.UserName = request.POST.get('parentName','')
            myusers.UserID = request.POST.get('parentID','')
            myusers.UserPW = request.POST.get('parentPW','')
            myusers.UserChild1ID = request.POST.get('childID','')
            myusers.UserChild1Name = request.POST.get('childName','')
            myusers.UserFlag = "Parent"
            myusers.save()
            
            return redirect('home')

    return render(request, 'parentSignup.html')


def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')

def map(request):
    CSs = Cs.objects
    FSs = Fs.objects
    OSs = Os.objects
    Dongs = Dong.objects
    cnt = 0
    cnt2 = 0
    cnt3 = 0
    address3 = request.POST.get('address3','')
    time_point = request.POST.get('time','')
    for a in CSs.all():
        if(address3 == a.distinct) :
            cnt=cnt+1

    for b in FSs.all():
        if(address3 ==b.distinct):
            if(b.time >= time_point):
                cnt2 = cnt2+1

    for c in OSs.all():
        if(address3 ==c.distinct):
            cnt3= cnt3+1
    return render(request, 'map.html', {'Css': CSs, 'Fss':FSs, 'Oss':OSs, 'Dongs':Dongs, 'address' : address3, 'cnt':cnt, 'cnt2': cnt2 , 'cnt3':cnt3, 'time_point':time_point})
def map2(request):
    CSs = Cs.objects
    FSs = Fs.objects
    OSs = Os.objects
    Dongs = Dong.objects

    return render(request, 'map2.html', {'Css': CSs, 'Fss':FSs, 'Oss':OSs, 'Dongs':Dongs})


def childMypage(request):
    childUser = Childuser.objects
    return render(request, 'childMypage.html', {'childUser' : childUser})

def parentMypage(request):

    parentUser = Parentuser.objects
    childUser = Childuser.objects
 

    return render(request, 'parentMypage.html',{'parentUser': parentUser , 'childUser' : childUser})