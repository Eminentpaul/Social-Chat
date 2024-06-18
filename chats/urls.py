from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>/chats/', views.get_user, name='receiver')
]
