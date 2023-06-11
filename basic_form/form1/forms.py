from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class usercf(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']