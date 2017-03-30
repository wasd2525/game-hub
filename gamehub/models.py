from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'static/img',blank=True, null=True)
    category = models.ForeignKey('gamehub.Category', null=True)
    slug = models.SlugField(max_length=100, db_index=True, default="Slug")

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def __str__(self):
        return self.catTitle

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    catTitle = models.CharField(max_length=100, db_index=True, null=True)
    slug = models.SlugField(max_length=100, db_index=True, default="Slug")


    def __str__(self):
        return self.catTitle



class Comment(models.Model):
    post = models.ForeignKey('gamehub.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text