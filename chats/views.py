from django.shortcuts import render, redirect
from accounts.models import Contact
from base.models import User
from .models import Message
from .forms import MessageForm
from accounts.models import Contact, FriendRequest
from datetime import datetime


# Create your views here.
def get_user(request, username):
    user = request.user
    friend_list = []
    contact_list = []

    friend_requests = FriendRequest.objects.filter(
        accepter=user, is_accepted=False)
    contacts = Contact.objects.all().filter(user=request.user)
    users = User.objects.all().exclude(email=user)

    receiver = User.objects.get(username=username)
    contact = Contact.objects.get(friend=receiver, user=request.user)

    for contact in contacts:
        contact_list.append(contact.friend.email)

    for user in users:
        if user.email not in contact_list:
            friend_list.append(user)

    full_messages = Message.objects.all()
    mg_list = []

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)

        if form.is_valid():
            data = Message()

            data.sender = request.user
            data.receiver = receiver
            data.body = form.cleaned_data.get('body')
            data.image = form.cleaned_data.get('image')
            data.save()

            data.chat_list.add(request.user)
            data.chat_list.add(receiver)

            return redirect('receiver', receiver.username)

    for mg in full_messages:
        if (mg.sender == request.user or mg.receiver == request.user) and (mg.sender == receiver or mg.receiver == receiver):
            mg_list.append(mg)

    messages = Message.objects.all().order_by('-created')

    list1 = []

    chat_list = []

    dt = datetime.today().date().strftime('%Y-%m-%d')

    for mg in messages:
        if mg.sender == request.user or mg.receiver == request.user:
            if list(mg.chat_list.all()) not in list1:
                list1.append(list(mg.chat_list.all()))
                chat_list.append(mg)

    for chat in chat_list:
        if chat.sender == receiver:
            chat.is_read = True
            chat.save()

    context = {
        'receiver': receiver,
        'full_messages': mg_list,
        'friend_requests': friend_requests,
        'contacts': contacts,
        'users': friend_list,
        'chat_list': chat_list,
        'dt': dt
    }
    return render(request, 'index.html', context)
