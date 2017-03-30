from django.contrib import admin
from .models import Post, Comment, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)