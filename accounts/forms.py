from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms



class CustomUserCreationForm(UserCreationForm):
    Ta_Classes = forms.CharField(max_length=100,label = "Ta Classes")
    Days = forms.CharField(max_length=50,label = "Days Avalible")
    Hours = forms.CharField(max_length=50)
    Bio = forms.CharField(max_length=200,label="Bio")
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "Ta_Classes",
            'Days',
            "Hours", 
            "Bio",                                
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = (
            "username",
            "email",
            "age",
                                             
        )
class hoursForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["Days",'Hours']



