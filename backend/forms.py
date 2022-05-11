from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')

        username = forms.CharField(
            min_length=3,
            max_length=12,
            label='Username',
            widget=forms.TextInput(attrs={'placeholder': 'ВВОДИ'}),
        )

        password = forms.CharField(
            min_length=3,
            max_length=12,
            label='Password',
            widget=forms.PasswordInput(attrs={'placeholder': 'ВВОДИ ПАРООЛЬ'}),
        )

        password_confirm = forms.CharField(
            min_length=3,
            max_length=12,
            label='Password Confirmation',
            widget=forms.PasswordInput(attrs={'placeholder': 'ВВОДИ ПАРОЛЬ СНОВА'}),
        )

        def clean(self):
            cleaned_data = self.cleaned_data
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')

            if password == password_confirm:
                return cleaned_data

            raise forms.ValidationError('ПАРОЛИ РАЗНЫЕ')

        def save(self, commit=True):
            user = super().save(commit=False)
            password = self.cleaned_data['password']
            user.set_password(password)
            if commit:
                user.save()
            return user