from django import forms
from user import models
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    photo = forms.ImageField(required=False, label='Фото профиля', widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=100, required=False, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повторите')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует")   
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует")   
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if models.Profile.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Пользователь с таким номером телефона уже существует")   
        return phone
    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['photo', 'phone']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    email = forms.EmailField(required=True, label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['email'].initial = kwargs['instance'].user.email
            self.fields['first_name'].initial = kwargs['instance'].user.first_name
            self.fields['username'].initial = kwargs['instance'].user.username
