from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import logout 
from django_email_verification import send_email
from principal.models import User,Pagos,TipoInversion
from principal.forms import UserForm,PagosForm,TipoInversionForm,UrbUserRegisterform
from .Reporteador import showCoins
from .Databases import saveUser, saveInver,savePagos

def inicio(request):
    showCoins(1)
    saveUser(1)
    saveInver(1)
    savePagos(1)
    context={
            'Donde':showCoins.Donde,
            'Dollars':showCoins.Dollars,
            'Euros':showCoins.Euros,
            'Shivas':showCoins.Shivas,
            'Ethers':showCoins.Ethers,
            'Bitcoins' :showCoins.Bitcoins,
            'Cardanos':showCoins.Cardanos,
    }
    return render (request,'index.html',context)

def login(request):
    return render(request,'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

def dashboard(request):
    if(request.user.is_authenticated):
        return render (request,'dashboard.html')
    else:
        return redirect('login')

def appsettings(request):
    if(request.user.is_authenticated):
        return render (request,'settings.html')
    else:
        return redirect('login')

def apphistory(request):
    if(request.user.is_authenticated):
        return render (request,'data-tbi.html')
    else:
        return redirect('login')

def applock(request):
    if(request.user.is_authenticated):
        return render (request,'lock.html')
    else:
        return redirect('login')

def notfound(request):
    if(request.user.is_authenticated):
        return render (request,'404.html')
    else:
        return redirect('login')

def account(request):
    if(request.user.is_authenticated):
        return render (request,'account-overview.html')
    else:
        return redirect('login')
    

def deposit(request):
    if(request.user.is_authenticated):
        render (request,'account-deposit.html')
    else:
        return redirect('login')
      
def register(request):
    if request.POST:
        
        form = UrbUserRegisterform(request.POST)
        if form.is_valid():
            
            user=form.save()
            user.is_active = False
            #send_email(user)

            return redirect('index')
        contexto = {
            'form': form
        }
    else:
        form = UrbUserRegisterform()
        contexto = {
            'form': form
        }
    return render(request, "signup.html",contexto)

def emailconfirmation(request):
    if request.POST:
        form = UserForm(request.POST)
        if request.POST.get('resend'):
            user= User.objects.get(email__exact=request.POST.get('email'))
            send_email(user)
            contexto= {
            'form': form
        }
            return render (request,'confirm-email.html',contexto)
    else:
        form=UserForm()
        contexto= {
            'form': form
        }
    return render(request, "confirm-email.html",contexto)
    
