from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        

class UpdateAccountImage(ModelForm):
    class Meta:
        model = User
        fields = ['image']