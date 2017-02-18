from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User




# Create your views here.

@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/chat.html?userid=&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat(request):
	username = '/chat.html?userid=&nickname=' + request.user.username

	if request.user.is_authenticated():
		return render(request, 'gamehub/chat.html', {})

	if request.get_full_path != username:
		return HttpResponseRedirect('/index/')



def login(request):
	return render(request, 'gamehub/login.html', {})

def register(request):
	return render(request, 'gamehub/register.html', {})



