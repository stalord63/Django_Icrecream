from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'number':3000
    }
    messages.success(request,'This is a test message')
    return render(request,'index.html',context)
def about(request):
   return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save() 
        messages.success(request, 'Your Information has reached to user!!')
    return render(request,'contact.html')


