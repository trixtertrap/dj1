from django.shortcuts import render
from .models import Contact
from .models import Query
from .models import EmployeeLogin
from .models import AdminLogin
from django.shortcuts import redirect, render



from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html",{})

def customer(request):
    return render(request,"customer.html",{})


def about(request):
    return render(request,"about.html",{})

def contact(request):
    if request.method=="POST":
        contact=Contact.objects.all()
        name=request.POST.get("nametxt")
        email=request.POST.get("emailtxt")
        phone=request.POST.get("phonetxt")
        suggestion=request.POST.get("suggesttxt")
        contact1=Contact(name=name,email=email,phone=phone,suggestion=suggestion)
        contact1.save()
        return render(request,"thankyou.html",{})
    else:
        return render(request,"contact.html",{})


def postquery(request):
    if request.method=="POST":
        query1=Query()
        name=request.POST.get("nametxt")
        email=request.POST.get("emailtxt")
        query=request.POST.get("querytxt")
        post1=Query(name=name,query=query,email=email)
        post1.save()
        qid=Query.objects.order_by('-id')[0];
        return render(request,"queryid.html",{"query1":qid})
    else:
        return render(request,"postquery.html",{})

def knowstatus(request):
    if request.method=="POST":
        knowid=Query.objects.all()
        queryid=request.POST.get("queryid")
        answer=Query.objects.get(id=queryid)
        return render(request,"statusanswer.html",{"answer":answer})
    else:
        return render(request,"knowstatus.html",{})

from .models import AdminLogin

def adminlog(request):
    if request.method=="POST":
        item=Contact.objects.all()
        password=request.POST.get("passwordtxt")
        if password=="admin":
            password1=AdminLogin(password=password)
            password1.save()
            items = Contact.objects.all()
            return render(request, "loginsuccess.html", {"items": items})
        else:
            return render(request,"wrongadmin.html",{})

    else:
        return render(request,"adminlog.html",{})


def viewsolutions(request):
    if request.method=="POST":
        sol=Query.objects.all()
        name=Query.objects.get("nametxt")
        query=Query.objects.get("querytxt")
        sol1=Query(name=name,query=query)
        sol1.save()
        return render(request,"viewsolutions.html",{"sol":sol})
    else:
        sol=Query.objects.all()
        return render(request,"viewsolutions.html",{"sol":sol})


def employee(request):
    if request.method=="POST":
        items=Query.objects.all()
        name=request.POST.get("nametxt")
        password=request.POST.get("passwordtxt")
        queryid=Query.objects.order_by('-id')[0];
        if password=="employee":
            emp=EmployeeLogin(name=name,password=password)
            emp.save()
            items = Query.objects.all()
            return render(request, "answer1.html", {"items": items})
        else:
            return render(request,"wrongadmin.html",{})
    else:
        return render(request,"employee.html",{})

def faq(request):
    items=Contact.objects.all()
    suggestion=request.POST.get("suggesttxt")
    return render(request,"faq.html",{})

def answer1(request):
    if request.method=="POST":

        items=Query.objects.all()
        return render(request,"answer1.html",{"items":items})





def faq(request):
    item=Query.objects.all()
    return render(request,"faq.html",{"item":item})

def delete(request, id):
    if request.method=="POST":
        item=Query.objects.all()
        id1 = Query.objects.get(pk = id)
        id1.delete()
        return HttpResponse('deleted')

def employeeanswer(request):
    if request.method=="POST":
        return render(request,"thankyou.html",{})











