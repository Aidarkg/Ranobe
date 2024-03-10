import random
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, View
from django.urls import reverse_lazy

from user import models
from user import forms


class RegisterView(View):
    def get(self, request):
         return render(
            request, 
            'user/register.html', 
            {'form': forms.RegisterForm()})
    
    def post(self, request):
        form = forms.RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            photo = form.cleaned_data['photo']
            phone = form.cleaned_data['phone']

            user = User.objects.create_user(
                first_name=first_name,
                username=username,
                email=email,
                password=password,
                is_active=False
            )

            models.Profile.objects.create(
                user=user,
                photo=photo,
                phone=phone
            )

            code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            models.SMSCode.objects.create(
                user=user,
                code=code
            )
            send_mail(
                'Код подтверждения регистрации',
                f'Ваш код подтверждения регистрации: {code}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            
            return redirect('verify')
        else:
            return render(request, 'user/register.html', {'form': form})
        

class VerifyView(View):
    def get(self, request):
        return render(request, 'user/verify.html', {'form': forms.VerifyForm()})
    
    def post(self, request):
        form = forms.VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if models.SMSCode.objects.filter(code=code).exists():
                sms_code = models.SMSCode.objects.get(code=code)
                sms_code.user.is_active = True
                sms_code.user.save()
                sms_code.delete()
                return redirect('login')
            else:
                form.add_error('code', 'Неверный код')

        return render(request, 'user/verify.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', {'form': forms.LoginForm()})
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data) # None or User object
            if user is not None:
                login(request, user)
                return redirect('book_list')
            else:
                form.add_error(None, 'Неправильный логин или пароль')

        return render(request, 'user/login.html', {'form': form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/profile.html', {'form': forms.ProfileForm()})
    def post(self, request):
        logout(request)
        return redirect('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile