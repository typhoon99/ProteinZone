from django.shortcuts import render
from .models import Supplement, Message
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'Shop/index.html',{})

def protein(request):
    return render(request,'Shop/protein.html',{})

def creatine(request):
    return render(request,'Shop/creatine.html',{})

def peanutButter(request):
    return render(request,'Shop/peanutButter.html',{})

def energyDrink(request):
    return render(request,'Shop/energyDrink.html',{})

def bcaa(request):
    return render(request,'Shop/bcaa.html',{})

def glutamine(request):
    return render(request,'Shop/glutamine.html',{})

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