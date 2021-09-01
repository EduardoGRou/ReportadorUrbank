from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import User

class UserList(ListView):
    model= User
    template_name='index.html'
class UserCreate(CreateView):
    model=User
    form_class=UserForm
    template_name='crear_user.html'
    success_url=reverse_lazy('index')

class UserUpate(UpdateView):
    model=User
    form_class=UserForm
    template_name='crear_user.html'
    success_url=reverse_lazy('index')

class UserDelete(DeleteView):
    model=User
    template_name='verificacion.html'
    success_url=reverse_lazy('index')