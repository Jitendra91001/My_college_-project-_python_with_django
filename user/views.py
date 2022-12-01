from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    cdata=category.objects.all()
    return render(request,'user/home.html',{"data":cdata})

def about(request):
    return render(request, 'user/about.html')

def contactus(request):
    status=False
    if request.method == 'POST':
        Name=request.POST.get("name","")
        Mobile = request.POST.get("mobile", "")
        Email=request.POST.get("email","")
        Message=request.POST.get("msg","")
        res=contact(name=Name, email=Email, mobile=Mobile, message=Message)
        res.save()
        status=True

    return render(request,'user/contactus.html',{'S':status})

def index(request):
    return render(request,'user/index.html')


def course(request):
    cdata=courses.objects.all()
    mydict={"c":cdata}

    return render(request,'user/course.html',mydict)

def placement(request):
    cdata=courses.objects.all().order_by('-id')
    a=request.GET.get('msg')
    pdata=""
    if a is None:
        pdata=placements.objects.all()
    else:
        pdata=placements.objects.filter(pcourse=a)

    return render(request,'user/placements.html',{"course":cdata,"placement":pdata})

def adminlogin(request):
    return render(request,'user/adminlogin.html')
def ourcourseslogin(request):
    return render(request,'user/ourcourses.html')

def imagegallery(request):
    #gdata=gallery.objects.all().order_by('-id')
    gdata=gallery.objects.filter()
    mydict={"d":gdata}

    return render(request,'user/gallery.html',mydict)


def recruiters(request):
    rdata=recruiterss.objects.all()
    mydict={"r": rdata}
    return render(request,'user/recruiters.html',mydict)

def ourcourses(request):
    coursedata=ourcourse.objects.all()
    mydict={"course":coursedata}
    return render(request, 'user/ourcourses.html',mydict)

