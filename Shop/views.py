from django.shortcuts import render
from .models import Supplement, Message
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'Shop/index.html',{})

def protein(request):
    products = Supplement.objects.filter(supplementType__icontains = 'protein').order_by('-createdOn')
    return render(request,'Shop/Products/protein.html',{'products':products})

def creatine(request):
    products = Supplement.objects.filter(supplementType__icontains = 'creatine').order_by('-createdOn')
    return render(request,'Shop/Products/creatine.html',{'products':products})

def peanutButter(request):
    products = Supplement.objects.filter(supplementType__icontains = 'peanut').order_by('-createdOn')
    return render(request,'Shop/Products/peanutButter.html',{'products':products})

def preWorkout(request):
    products = Supplement.objects.filter(supplementType__icontains = 'pre workout').order_by('-createdOn')
    return render(request,'Shop/Products/preWorkout.html',{'products':products})

def bcaa(request):
    products = Supplement.objects.filter(supplementType__icontains = 'bcaa').order_by('-createdOn')
    return render(request,'Shop/Products/bcaa.html',{'products':products})

def about(request):
    return render(request,'Shop/about.html',{})
    
def mailUs(request):
    if request.method == "POST":
        message = Message()
        message.name = request.POST.get('name')
        message.phone_number = request.POST.get('name')
        message.email = request.POST.get('email')
        message.message = request.POST.get('message')
        message.save()

        subject = 'ProteinZone - ' + 'New Message from ' + str(message.name)
        message = 'Email: ' + str(message.email) + '\n' +'Phone: ' + str(message.phone_number) + '\n\n' + str(message.message)
        recepient = 'son.goku.db7@gmail.com'
        send_mail(subject, message, EMAIL_HOST_USER,[recepient], fail_silently = False)
        return render(request,'Shop/mailUs.html', {'message' : message})
    else:
        return render(request,'Shop/mailUs.html',{})