from django.shortcuts import render
from django.utils import timezone
from django.db import models
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404




#clash
@login_required(login_url='login')
def clash(request):
    if request.user.is_authenticated():
        username = '/chat.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat(request):
    categories = Category.objects.all(),
    posts = Post.objects.filter(category=1, published_date__lte=timezone.now()).order_by('published_date')
    posts2 = Post.objects.filter(slug="Slug1")
    username = '/chat.html?userid=&nickname=' + request.user.username

    return render(request, 'gamehub/chat.html', {
        'posts' : posts,
        'posts2' : posts2,
        #'liked': liked,
    })

   #end clash

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





#play
@login_required(login_url='login')
def play(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/play.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat1(request):
    categories = Category.objects.all(),
    posts = Post.objects.filter(category=3)
    posts2 = Post.objects.filter(slug="Slug1")
    username = '/play.html?userid=&nickname=' + request.user.username
    
  

    return render(request, 'gamehub/play.html', {
        'posts' : posts,
        'posts2' : posts2,
        
    })


	
#end play

#Xbox
@login_required(login_url='login')
def xbox(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/xbox.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat3(request):
    categories = Category.objects.all(),
    posts = Post.objects.filter(category=4)
    posts2 = Post.objects.filter(slug="Slug1")
    username = '/xbox.html?userid=&nickname=' + request.user.username

    return render(request, 'gamehub/xbox.html', {
        'posts' : posts,
        'posts2' : posts2,
        
    })


#end xbox


#steam
@login_required(login_url='login')
def steam(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.user.is_authenticated():
        username = '/steam.html?userid=' + request.user.username + '&nickname=' + request.user.username
    return redirect(username)

@login_required(login_url='login')
def chat2(request):
    categories = Category.objects.all(),
    posts = Post.objects.filter(category=5)
    posts2 = Post.objects.filter(slug="Slug1")
    username = '/chat.html?userid=&nickname=' + request.user.username

    return render(request, 'gamehub/steam.html', {
        'posts' : posts,
        'posts2' : posts2,
        
    })

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


#like button
"""def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            print("unlike")
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.likes + 1
    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)"""






def login(request):
	return render(request, 'gamehub/login.html', {})

def register(request):
	return render(request, 'gamehub/register.html', {})

def home(request):
	return render(request, 'gamehub/home.html', {})


