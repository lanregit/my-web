from django.contrib import admin
from blog.models import Category, Post, CompleteUser_Profile, Comment_user

# Register your models here.

admin.site.register(Category)
admin.site.register(CompleteUser_Profile)
admin.site.register(Post)
admin.site.register(Comment_user)

