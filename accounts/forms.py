from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from .models import Profile
import datetime


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
    def clean_email(self):
        if self.cleaned_data["email"] == "":
            raise ValidationError("Email is Required")
        return self.cleaned_data["email"]
    def save(self, data, commit=True):
        user = User.objects.create_user(data["username"], data["email"], data["password1"])
        user.is_active = False
        profile = Profile.objects.create(key=data["key"], user=user, key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=1) , "%Y-%m-%d %H:%M:%S") )
        user.save()
        profile.save()
        return user