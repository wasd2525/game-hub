from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
	url(r'^register/$', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    #clash
    url(r'^clash$', views.clash, name='clash'),
    url(r'^chat.html$', views.chat, name='chat'),




    #playstation
    url(r'^play$', views.play, name='play'),
    url(r'^play.html$', views.chat1, name='chat1'),

    #General
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.home, name='home'),

    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),

]
