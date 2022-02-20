from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile , Payment , Subscription
from django import forms
from django.core.exceptions import ValidationError

from django.db import transaction


class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username' , 'password1', 'password2']




    def __init__(self, *args , **kwargs):
        super(customUserCreationForm,self).__init__(*args,**kwargs)

        self.fields['first_name'].widget.attrs.update({'class':'input','placeholder': 'نام '})
        self.fields['last_name'].widget.attrs.update({'class':'input','placeholder': 'نام خانوادگی '})
        self.fields['email'].widget.attrs.update({'class': 'input', 'placeholder': 'ایمیل '})
        self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder': 'نام کاربری '})
        self.fields['password1'].widget.attrs.update({'class': 'input', 'placeholder': 'رمز '})
        self.fields['password2'].widget.attrs.update({'class': 'input', 'placeholder': 'تایید رمز'})



class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','name','familyName','email',
                  'username',
                  ]

    def __init__(self, *args, **kwargs):
        super(profileForm,self).__init__(*args,**kwargs)

        self.fields['name'].widget.attrs.update({'class':'input','placeholder': 'نام '})
        self.fields['familyName'].widget.attrs.update({'class':'input','placeholder': 'نام خانوادگی '})
        self.fields['email'].widget.attrs.update({'class': 'input', 'placeholder': 'ایمیل '})
        self.fields['username'].widget.attrs.update({'class': 'input disabled', 'placeholder': 'یوزرنیم '})
        self.fields['profile_image'].widget.attrs.update({'class': 'input','type':'file'})



class buySubsForm(ModelForm):
    class Meta:
        model = Subscription
        fields =['subscriptions',]


    def __init__(self, *args, **kwargs):
        super(buySubsForm,self).__init__(*args,**kwargs)

        self.fields['subscriptions'].widget.attrs.update({'class':'input orm-control form-control-lg',})


