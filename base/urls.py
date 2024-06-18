from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/<str:pk>/update/', views.accountUpdate, name='update'),
    path('logout/', views.logout, name='logout'),
    
    #PASSWORD MANAGEMENT
    
    #To Submit an email form
    path('user/reset/password/',
         auth_views.PasswordResetView.as_view(template_name='forgotten-password.html'), name='reset-password'),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset-email-sent.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset-password.html'), name='password_reset_confirm'),
    
    path('user/reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password-reset-complete.html'), name='password_reset_complete')
]
