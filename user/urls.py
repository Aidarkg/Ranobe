from django.urls import path
from user import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile')
]