from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages as mg
import requests
from .forms import UserForm, UpdateAccountImage
from .models import User
from django.contrib.auth.decorators import login_required
from accounts.models import FriendRequest, Contact



# Create your views here.
@login_required(login_url='login')
def feeds(request):
    user = request.user
    contact_list = []
    user_list = []

    friend_requests = FriendRequest.objects.filter(
        accepter=user, is_accepted=False)
    
    contacts = Contact.objects.all().filter(user=request.user)
    users = User.objects.all().exclude(email=user)

    for contact in contacts:
        contact_list.append(contact.friend.email)

    for user in users:
        if user.email not in contact_list:
            user_list.append(user)
    
    context = {
        'friend_requests': friend_requests,
        'contacts': contacts,
        'users': user_list,
    }
    return render(request, 'base/index.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('feeds')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            user.is_online = True
            user.save()
            
            auth.login(request, user)
            
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                mg.success(request, 'You Successfully Logged In!')
                return redirect('feeds')
        else:
            mg.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')


def register(request):
    error_msg = ''
    username = ''
    email = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            
            user.is_online = True
            user.save()
            
            # chat_list = ChatList.objects.filter(owner=user).exists()

            # if not chat_list:
            #     ChatList.objects.create(owner=user)
            auth.login(request, user)
            
            mg.success(request, 'Login Successful')
            return redirect('feeds')

        else:
            errors = form.errors.get_json_data(escape_html=True)
            for error in errors:
                error_msg = errors[error][0]['message']

            mg.error(request, error_msg)

    context = {
        'username': username,
        'email': email
    }
    return render(request, 'register.html', context)


@login_required(login_url='login')
def accountUpdate(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateAccountImage(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('chats')

def logout(request):
    if request.user.is_authenticated:
        user = request.user
        user.is_online = False
        user.save()
        auth.logout(request)
        mg.success(request, 'Logged Out Successfully')
        return redirect('login')

