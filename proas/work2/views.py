from django.shortcuts import render,redirect
from django.http import HttpResponse
from .formsign import signn,login
from .models import signupp

# Create your views here.

def signUp(request):

    if request.method == 'POST':
        
        form = signn(request.POST)
        log = login()
        if form.is_valid():
            form.save()
            return render(request,'signform.html',{'suc':'Login Sucess Full'})
            
        else:
            
            return render(request,'signform.html',{'suc':'Invalid Details'})
    
    form = signn()
    return render(request,'signform.html',{'form':form})

def log(request):
    
    if request.method == 'POST':
        
        form = login(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        u = signupp.objects.filter(username=username,password=password)

        
        if(u):
            return redirect('work:home')
    
        
        else:
            form = login()

            return render(request,'Login.html',{'form':form})


        

        


    else:

        form = login()

        return render(request,'Login.html',{'form':form})
    

    



   