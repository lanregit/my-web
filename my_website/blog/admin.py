from django.contrib import admin
from blog.models import Category, Post, CompleteProfile, Comments

# Register your models here.

admin.site.register(Category)
admin.site.register(CompleteProfile)
admin.site.register(Post)
admin.site.register(Comments)

