from django import forms
from .models import User,Pagos,TipoInversion,UrbUser
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'

class TipoInversionForm(forms.ModelForm):
    class Meta:
        model = TipoInversion
        fields = '__all__'


class UrbUserRegisterform(UserCreationForm):
    class Meta:
        model = UrbUser
        fields = ('username','firstname', 'lastname', 'email','phone')
        #fields= '__all__'
