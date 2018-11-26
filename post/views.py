from django.shortcuts import render
from .forms import FriendForm
from django.views.generic import TemplateView
from .models import Friend, Message
from django.shortcuts import redirect
from .forms import CheckForm
from .forms import FriendForm, MessageForm
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    data = Friend.objects.all().values()
    params = {
        'title': 'Post',
        'data': data
    }
    return render(request, 'post/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance = obj)
        friend.save()
        return redirect(to='/post')
    params = {
        'title': 'Hello',
        'form': FriendForm()
    }
    return render(request, 'post/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/post')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj)
    }
    return render(request, 'post/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend.delete()
        return redirect(to='/post')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend
    }
    return render(request, 'post/delete.html', params)

def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validates',
        'form': FriendForm()
    }
    if (request.method  == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK'
        else:
            params['message'] = 'No good'
    return render(request, 'post/check.html', params)


def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 3)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page)
    }
    return render(request, 'post/message.html', params)