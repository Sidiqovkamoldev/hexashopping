from django import forms
from .models import  Client, ClientModel





class ClientForm(forms.ModelForm):

    class Meta:
        model=Client
        fields=["name", "phone"]


class ClientModelForm(forms.ModelForm):

    class Meta:
        model=ClientModel
        fields="__all__"
