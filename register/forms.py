from django import forms
from .models import *


class UserRegisterForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['name', 'phoneNum', 'tableNo']
    labels = {
      "name": "",
      "phoneNum": "",
      "tableNo": "",
    }
    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Your Name','required':'required'}),
        'tableNo':forms.NumberInput(attrs={'placeholder':'Your Table Number','required':'required','min':1,'max':25}),
        'phoneNum':forms.NumberInput(attrs={'placeholder':'Your Contact Number','required':'required'}),
    }
