from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib import messages as mg
from .models import FriendRequest, Contact, Profile
from django.db import transaction
from base.models import User
from chats.models import Message
from datetime import datetime
# Create your views here.


@login_required(login_url='login')
def chats(request):
    user = request.user

    if not user.is_online:
        return redirect('login')
    friend_list = []
    contact_list = []

    

    mg_list = []

    messages = Message.objects.all().order_by('-created')

    list1 = []

    chat_list = []

    for mg in messages:
        if mg.sender == request.user or mg.receiver == request.user:
            if list(mg.chat_list.all()) not in list1:
                list1.append(list(mg.chat_list.all()))
                chat_list.append(mg)

    dt = datetime.today().date().strftime('%Y-%m-%d')

    context = {
        'chat_list': chat_list,
        'dt': dt
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def profile(request, pk):
    profile = User.objects.get(id=pk)
    followers = Profile.objects.all()
    number_of_following = 0
    is_follower = False

    for n in followers:
        if profile == request.user:
            if request.user in n.followers.all():
                number_of_following += 1
        else:
            if profile in n.followers.all():
                number_of_following += 1

    if request.user in profile.profile.followers.all():
        is_follower = True

    context = {
        'profile': profile,
        'followers': profile.profile.followers.all(),
        'number_of_following': number_of_following,
        'contacts': Contact.objects.filter(user=profile),
        'is_follower': is_follower
    }
    return render(request, 'accounts/public-profile-about.html', context)


@login_required(login_url='login')
def edit_profile(request, username):
    user = request.user
    profile = user.profile
    form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    return render(request, 'accounts/edit-profile.html', {'form': form})


@login_required(login_url='login')
def connections(request, pk):
    profile = User.objects.get(id=pk)
    followers = Profile.objects.all()

    following = []
    is_follower = False

    for n in followers:
        if profile == request.user:
            if request.user in n.followers.all():
                following.append(n)
        else:
            if profile in n.followers.all():
                following.append(n)

    if request.user in profile.profile.followers.all():
        is_follower = True

    context = {
        'profile': profile,
        'followers': profile.profile.followers.all(),
        'following': following,
        'following_count': len(following),
        'contacts': Contact.objects.filter(user=profile),
        'is_follower': is_follower
    }
    return render(request, 'accounts/profile-connections.html', context)


@login_required(login_url='login')
def friend_requests(request):
    user = request.user
    friend_requests = FriendRequest.objects.filter(
        accepter=user, is_accepted=False)
    
    context = {
        'friend_requests': friend_requests,
        'owner': True,
    }
    return render(request, 'accounts/friend-request.html', context)


@login_required(login_url='login')
def all_users(request):
    user = request.user 
    user_list = []
    contact_list = []
    
    my_requests = FriendRequest.objects.all().filter(sender=user)

    contacts = Contact.objects.all().filter(user=request.user)
    users = User.objects.all().exclude(email=user)

    for contact in contacts:
        contact_list.append(contact.friend.email)

    for user in users:
        if user.email not in contact_list:
            user_list.append(user)
            
            
    print(user_list)
    context = {
        'user_list': user_list,
        'my_requests': my_requests
    }
    
    return render(request, 'accounts/suggestions.html', context)


@login_required(login_url='login')
def add_follower(request, pk):
    owner = User.objects.get(id=pk)
    owner.profile.followers.add(request.user)
    return redirect('profile', owner.id)


@login_required(login_url='login')
def unfollow(request, pk):
    owner = User.objects.get(id=pk)
    owner.profile.followers.remove(request.user)
    return redirect('profile', owner.id)


@login_required(login_url='login')
def profileUpdate(request):
    user = request.user
    error_msg = ''
    if request.method == 'POST':
        form = UpdateAccount(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            mg.success(request, 'Updated Successfully')
            return redirect('chats')
        else:
            errors = form.errors.get_json_data(escape_html=True)
            for error in errors:
                error_msg = errors[error][0]['message']

            mg.error(request, error_msg)
            return redirect('profile', request.user.id)


@login_required(login_url='login')
def addFriend(request, pk):
    accepter = User.objects.get(id=pk)
    sender = request.user

    FriendRequest.objects.create(
        sender=sender,
        accepter=accepter
    )

    return redirect('all_users')


@login_required(login_url='login')
def acceptRequest(request, pk):
    try:
        freind_request = FriendRequest.objects.get(
            id=pk, is_accepted=False, accepter=request.user)

    except FriendRequest.DoesNotExist:
        pass

    with transaction.atomic():
        freind_request.is_accepted = True
        freind_request.save()

        Contact.objects.create(
            user=request.user,
            friend=freind_request.sender
        )
        Contact.objects.create(
            user=freind_request.sender,
            friend=request.user
        )

    return redirect('feeds')


@login_required(login_url='login')
def rejectRequest(request, pk):
    obj = FriendRequest.objects.get(id=pk)
    obj.delete()
    
    url = request.META.get('HTTP_REFERER')
    return redirect(str(url))
