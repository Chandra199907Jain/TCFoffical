from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from bakes.settings import EMAIL_HOST_PASSWORD
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from .models import Register

def index(request):
    return render(request,'tcf/index.html')
def about(request):
    return render(request,'tcf/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        message = request.POST.get("message")
        print("POST")
        print(name)
        print(email)
        print(message)
        email_to=EMAIL_HOST_PASSWORD
        email=EmailMessage(
            name,
            email,
            message,
             [email_to],
            reply_to=[email],
        )
        email.send()
        
    return render(request,'tcf/contact.html')
def faq(request):
    return render(request,'tcf/contact.html')
def minicake(request):
    return render(request,'tcf/minicake.html')
def partycake(request):
    return render(request,'tcf/partycake.html')
def themecake(request):
    return render(request,'tcf/themecake.html')
def tier(request):
    return render(request,'tcf/tier.html')
def cupcakes(request):
    return render(request,'tcf/cupcakes.html')
def cookies(request):
    return render(request,'tcf/cookies.html')
def register(request):
    if request.method == 'POST':
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        print("POST")
        values={
            'name':name,'email':email,'password':password
               }
        registers=Register(name=name,email=email,password=password)
        error_message=None
        if len(registers.name)<2:
            error_message="Length of the name should be greater than 2"
        if len(registers.password)<8:
            error_message="password should be more than 7characters"

        if not error_message:
            if Register.objects.filter(name=name).exists():
                error_message="Username taken"
                return redirect("index")
            elif Register.objects.filter(email=email).exists():
                error_message="Email taken"
                return redirect("index")
            else:
                registers.password = make_password(registers.password)
                registers.save()
                print("No errors")
                return redirect("index")

        else:
            data = {
                'error':error_message,'values':values
                 }
            print("Errors")
            return render(request,"tcf/register.html",data)
        
        
    else:
        print("GET")
        return render(request,'tcf/register.html')





