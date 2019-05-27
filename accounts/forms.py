from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar')

    def clean_password(self):
        password = self.cleaned_data['password']
        return make_password(password)
