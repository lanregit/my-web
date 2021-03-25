from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver
# import uuid
# Create your models here.


# model for category
class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='post category')
    cat_des = models.TextField(verbose_name='Category Description', blank=True)

    def __str__(self):
        return self.category


# model for post
class Post(models.Model):
    title = models.TextField(verbose_name='Post Title')
    cat = models.ManyToManyField(Category, verbose_name='Select Post Category')
    img = models.ImageField(verbose_name='picture', upload_to= 'images', blank=True, null=True)
    content = models.TextField(verbose_name='Post',)
    poster = models.ForeignKey(User, verbose_name='Post By', on_delete=models.CASCADE, default=User)
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)
    time = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField(verbose_name='Approve Post', default=False)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count

# model for CompleteProfile
class CompleteUser_Profile(models.Model):

    Male = 'ML' 
    Female = 'FM'
    Gender = [
        (Male, 'male'),
        (Female, 'female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=2, choices=Gender, blank=False, null=True, default=Male)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Profile Picture')
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# model for comment
class Comment_user(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_by= models.ForeignKey(User, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(verbose_name="Users' Comment")
    reply = models.ForeignKey('Comment_user', null=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return self.comment


