from django import forms
from .models import signupp




class signn(forms.ModelForm):

    class Meta:
        model = signupp
        fields = '__all__'


        
class login(forms.ModelForm):
    class Meta:

        model = signupp
        exclude = ['Email','Mobile']