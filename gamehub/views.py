from django.shortcuts import render
from django.utils import timezone
from django.db import models
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404







#clash
@login_required(login_url='login')
def clash(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/chat.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	username = '/chat.html?userid=&nickname=' + request.user.username


	if request.user.is_authenticated():
		return render(request, 'gamehub/chat.html', {'posts' : posts})

	if request.get_full_path != username:
		return HttpResponseRedirect('/index/')

	 
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.publish()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'gamehub/post_edit.html', {'form': form})

    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'gamehub/post_detail.html', {'post': post})


#end clash



#play
@login_required(login_url='login')
def play(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/play.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat1(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	username = '/play.html?userid=&nickname=' + request.user.username

	if request.user.is_authenticated():
		return render(request, 'gamehub/play.html', {'posts' : posts})

	
#end play

#steam
@login_required(login_url='login')
def steam(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/steam.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat2(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	username = '/steam.html?userid=&nickname=' + request.user.username

	if request.user.is_authenticated():
		return render(request, 'gamehub/steam.html', {'posts' : posts})

	
#end steam



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.approve()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'gamehub/add_comment_to_post.html', {'form': form})

   
def pagination_ajax(request, pk=None):
    if not request.is_ajax():
        return Http404()

    if pk is not None:
        # I'm doing an extra query because datetime serialization/deserialization is hard
        date = timezone.now()
    else:
        # is requesting the first page
        date = None

    posts = Post.objects.all()
    paginator = SeekPaginator(posts, per_page=5, lookup_field='date')

    try:
        page = paginator.page(value=date, pk=pk)
    except EmptyPage:
        data = {'error': "this page is empty", }
    else:
        posts_list = [{"title": a.title, } for a in page]
        data = {'articles': posts_list,
                'has_next': page.has_next(),
                'pk': page.next_page_pk()}

    return HttpResponse(json.dumps(data), content_type="application/json")



def login(request):
	return render(request, 'gamehub/login.html', {})

def register(request):
	return render(request, 'gamehub/register.html', {})

def home(request):
	return render(request, 'gamehub/home.html', {})

