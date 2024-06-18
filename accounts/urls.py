from django.urls import path 
from . import views

urlpatterns = [
    path('chat/', views.chats, name='chats'),
    path('accept/<str:pk>/user/', views.acceptRequest, name='accept'), 
    path('reject/<str:pk>/user/', views.rejectRequest, name='reject'), 
    path('add/<str:pk>/user/', views.addFriend, name='add'), 
    path('update/account', views.profileUpdate, name='update-profile'),
]
