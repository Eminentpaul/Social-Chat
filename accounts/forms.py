from django.forms import ModelForm
from base.models import User


class UpdateAccount(ModelForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'email', 'location']
