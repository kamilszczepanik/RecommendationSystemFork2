from django import forms
from .models import Users
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['login', 'display_name', 'password']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        password_hash = make_password(self.cleaned_data['password'])
        user.password_hash = password_hash.encode('utf-8')
        if commit:
            user.save()
        return user
