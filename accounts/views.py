from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateAccount
from django.contrib import messages as mg
from .models import FriendRequest, Contact
from django.db import transaction
from base.models import User
from chats.models import Message
from django.db.models import Max, Count
from datetime import datetime
# Create your views here.


@login_required(login_url='login')
def chats(request):
    user = request.user

    if not user.is_online:
        return redirect('login')
    friend_list = []
    contact_list = []

    friend_requests = FriendRequest.objects.filter(
        accepter=user, is_accepted=False)
    contacts = Contact.objects.all().filter(user=request.user)
    users = User.objects.all().exclude(email=user)

    for contact in contacts:
        contact_list.append(contact.friend.email)

    for user in users:
        if user.email not in contact_list:
            friend_list.append(user)

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
        'friend_requests': friend_requests,
        'contacts': contacts,
        'users': friend_list,
        'chat_list': chat_list,
        'dt': dt
    }

    return render(request, 'index.html', context)


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
            return redirect('chats')


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

    return redirect('chats')


def addFriend(request, pk):
    accepter = User.objects.get(id=pk)
    sender = request.user

    FriendRequest.objects.create(
        sender=sender,
        accepter=accepter
    )

    return redirect('chats')


def rejectRequest(request, pk):
    obj = FriendRequest.objects.get(id=pk)
    obj.delete()
    return redirect('chats')
