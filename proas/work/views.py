from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import emailu
import google.generativeai as genai
from django.conf import settings




genai.configure(api_key=settings.GEMINI_API_KEY)


# Create your views here.

def Show(request):

    return HttpResponse("Hello, World!")

def show2(request):

    return render(request,'home.html')

def send_maill(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')
        fromaddress = request.POST.get('fromaddress')
        toaddress = request.POST.get('toaddress')

        print(subject,message_body,fromaddress,toaddress)
        send_mail(subject,message_body,fromaddress,[toaddress],fail_silently=False)

        try:

            

            emailu.objects.create(subject=subject,message=message_body,fromaddress=fromaddress,toaddress=toaddress)
            messages.success(request, 'Mail sent successfully!')
            return render(request, 'mail.html')
        except:
            messages.error(request, 'Mail failed to send!')
            return render(request, 'mail.html')

def show_mail(request):
        
        if request.method == 'POST':
            subject = request.POST.get('subject')
            message_body = request.POST.get('message')
            fromaddress = request.POST.get('fromaddress')
            toaddress = request.POST.get('toaddress')
            

            print(subject,message_body,fromaddress,toaddress)
            
            

            try:
                send_mail(subject,message_body,fromaddress,[toaddress],fail_silently=False)

                
                emailu.objects.create(subject=subject,message=message_body,fromaddress=fromaddress,toaddress=toaddress)
                
               
                return render(request, 'mail.html',{'message':'M A I L   S E N T  S U C C E S S'})
            
            except:
                
                return render(request, 'mail.html',{'message':'M A I L   S E N T  F A I L E D'})

        return render(request,'mail.html')




def text_ai(request):
    if request.method == 'POST':
        
        prompt = request.POST.get('name')
    
        if prompt:

            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(prompt)
            result = response.text

            print(result)

            return render(request,'textai.html',{'result':result})
        else:
            return render(request,'textai.html',{'result':'Connection error'})
    else:
        return render(request,'textai.html',{'result':'Wait for Answer'})

 