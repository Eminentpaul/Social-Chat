from django.urls import path 
from . import views

urlpatterns = [
    path('chat/', views.chats, name='chats'),
    path('accept/<str:pk>/user/', views.acceptRequest, name='accept'), 
    path('user/<str:pk>/profile/', views.profile, name='profile'), 
    path('user/<str:pk>/connections/', views.connections, name='connections'),
    path('user/<str:username>/edit-profile/', views.edit_profile, name='edit_profile'), 
    path('reject/<str:pk>/user/', views.rejectRequest, name='reject'), 
    path('add/<str:pk>/user/', views.addFriend, name='add'), 
    path('user/friend-requests', views.friend_requests, name='friend_requests'),
    path('all/users', views.all_users, name='all_users'), 
    path('update/account', views.profileUpdate, name='update-profile'),
    path('follow/<str:pk>/', views.add_follower, name='follow'),
    path('unfollow/<str:pk>/', views.unfollow, name='unfollow'),
]
