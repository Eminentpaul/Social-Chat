from django.forms import ModelForm
from .models import Profile


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers'] 
