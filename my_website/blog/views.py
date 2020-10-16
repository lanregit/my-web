from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from blog.blog_form import SignUp, CompleteProfileForm, PostForm, EditProfile, CommentForm, UpdatePostForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post, Category, Comment_user, CompleteUser_Profile 
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# view for blog homepage
def blog(request):
    category = Category.objects.all() 
    blog_post = Post.objects.all().order_by('-time')
    args = {'post':blog_post, 'cate':category}
    return render (request, 'blog/blog.html', args)

# view for read_more page
def post_read(request, pos_id):
    category = Category.objects.all()
    post = Post.objects.get(id=pos_id)
    comments = Comment_user.objects.filter(post=post).order_by('comment_time')
    return render(request, 'blog/read_post.html', {'post':post, 'comments':comments, 'cate':category})

# view for login homepage
@login_required
def blog_login(request):
    category = Category.objects.all()
    blog_post = Post.objects.all().order_by('-time')
    args = {'post':blog_post, 'cate':category, 'prof':request.user}
    return render(request, 'blog/blog_login.html', args)

# view for read_more (login) page
    

@login_required
def login_post_read(request, pos_id):
    cat = Category.objects.all()
    user = request.user
    comment_user = Comment_user.objects.all()
    post = get_object_or_404(Post, id=pos_id)
    comments = Comment_user.objects.filter(post=post, reply=None)
    # comment_lk = get_object_or_404(Comment_user, id=request.POST.get(comments))
    #post likes
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    #comment likes
    # liked = False
    # if comment_lk.likes.filter(id=request.user.id).exists():
    #     liked = True
    if request.method == 'POST':
        user_comment = CommentForm(request.POST or None)
        if user_comment.is_valid:
            comment = request.POST.get('comment')
            reply_id = request.POST.get('c_id')
            reply_qs = None
            if reply_id:
                reply_qs = Comment_user.objects.get(id=reply_id)
            content = Comment_user.objects.create(post=post, comment_by=request.user, comment=comment, reply=reply_qs)
            content.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_comment = CommentForm(request.POST)
    content = {
        'post':post,
        'comment':comments,
        'comment_form':user_comment,
        'cate':cat,
        'is_liked':is_liked,
        'total_likes':post.total_likes(),
        # 'comment_lk':comment_lk,
        # 'liked':liked,
        # 'total_comment_likes':comment_lk.count_like(),
    }
    return render(request, 'blog/login_read_post.html', content)

# view for post likes
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return redirect('blog:login_read_post', post.id)

# view for comment likes
def comment_like(request):
    comment_lk = get_object_or_404(Comment_user, id=request.POST.get('user_id'))
    liked = False
    if comment_lk.likes.filter(id=request.user.id).exists():
        comment_lk.likes.remove(request.user)
        liked = False
    else:
        comment_lk.likes.add(request.user)
        liked= True
    return redirect('blog:login_read_post', comment_lk.post.id)

# view for Register (signup) page
def register(request):
    # com = CompleteProfileForm()
    if request.method == 'POST':
        sign = SignUp(request.POST)
        if sign.is_valid():
            sign.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('/lanre_blog/user_profile/')
    else:
        sign = SignUp()
    return render(request, 'blog/signup.html', {'up':sign, 'com':complete})

# view user's profile
def my_profile(request):
    my_post = Post.objects.filter(poster = request.user)
    my_comment = Comment_user.objects.filter(comment_by = request.user)
    return render(request, 'blog/profile.html', {'prof':request.user, 'post':my_post, 'comment':my_comment})

# view for more user informatiom
@login_required
def complete_profile(request):
    if request.method == 'POST':
        complete = CompleteProfileForm(request.POST, request.FILES)
        if complete.is_valid():
            com_prof = complete.save(commit=False)
            com_prof.user = request.user
            complete.save()
            return redirect('blog:profile') 
    else:
        complete = CompleteProfileForm(request.POST, request.FILES)
    return render(request, 'blog/complete.html', {'com':complete})

# request for complete profile
def complete(request):
    return render(request, 'blog/complete_profile.html')

#VIEW FOR EDITPROFILE
@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit = EditProfile(request.POST, request.FILES, instance=request.user)
        if edit.is_valid():
            edit.save()
            return redirect('blog:profile')
    else:
        edit = EditProfile(instance=request.user)
    return render(request, 'blog/edit-profile.html', {'edit':edit})

#VIEW FOR USER CREATE POST
@login_required
def user_post(request):
    if request.method == 'POST':
        post_news = PostForm(request.POST, request.FILES)
        if post_news.is_valid():
            p_user = post_news.save(commit=False)
            p_user.poster = request.user
            post_news.save() 
            return redirect('blog:blog_l')
    else:
        post_news = PostForm(request.POST, request.FILES)
    return render(request, 'blog/user_post.html', {'userpost':post_news})


#view for post according to category
def category(request, cats):
    categori = Category.objects.all()
    post = Post.objects.filter(cat__category=cats)
    if request.method == 'POST':
        post_news = PostForm(request.POST, request.FILEs)
        if post_news.is_valid():
            cat_post = post_news.save(commit=False)
            cat_post.poster = request.user
            cat_post.cat = cats
            post_news.save()
            return redirect ('blog:category', cats)
        else:
            post_news = PostForm(request.POST, request.FILES)
    args = {'cats':cats, 'post':post, 'cate':categori}
    return render(request, 'blog/category.html', args)


# view for user update post
@login_required
def updatepost(request, id):
    post = get_object_or_404(Post, id=id)
    if post.poster == request.user:
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:login_read_post', id)
    return render(request, 'blog/updatepost.html', {'form':form}) 


# view for delete post
@login_required
def delete_post(request, id):
    post = Post.objects.get(id = int(id))
    if post.poster == request.user:
        post.delete()
        return redirect('blog:blog_l')
    else:
        return Http404('Only the Author of this post can delete it')
    

def confirm_post(request):
    return render (request, 'blog/deletepost.html')

# view for user comment update
@login_required
def updatecomment(request, id):
    comment = get_object_or_404(Comment_user, id=id)
    if comment.comment_by == request.user:
        update = CommentForm(request.POST or None, instance=comment)
        if update.is_valid():
            update.save()
            return redirect('blog:login_read_post', comment.post.id)
    return render(request, 'blog/updatecomment.html', {'update':update})

#view for delete comment
@login_required
def delete_comment(request, id):
    comment = Comment_user.objects.get(id=id)
    comment.delete()
    return redirect('blog:login_read_post', comment.post.id)

# view for to each user profile
def userprofile (request, username):
    person = get_object_or_404(User, username=username)
    # my_post = Post.objects.filter(poster_id=username)
    context = {'per':person,}
    return render(request, 'blog/userprofile.html', context)       

# def userprofile(request, username):
#     person = User.objects.get(username=username)
#     my_post = Post.objects.filter(poster=username)
#     my_comment = Comment_user.objects.filter(comment_by=username)
#     return render(request, 'blog/userprofile.html', {'per':person, 'com':my_comment, 'post':my_post})       

# VIEW FOR USERS' PROFILE
# def profile(request, User):
#     user = User.objects.get(name=User.username)
#     return render(request, 'blog/userprofile.html', {'user2':user})


# @login_required
# def login_post_read(request, pos_id):
#     cat = Category.objects.all()
#     post = get_object_or_404(Post, id=pos_id)
#     is_liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         is_liked = True
#     comment = Comment_user.objects.filter(post=post)
#     if request.method == 'POST':
#         user_comment = CommentForm(request.POST)
#         if user_comment.is_valid:
#             usercomment = user_comment.save(commit=False)
#             usercomment.post = post
#             usercomment.comment_by = request.user
#             user_comment.save(commit=True)
#             return HttpResponseRedirect(request.path_info)
#     else:
#         user_comment = CommentForm(request.POST)
#     content = {
#         'post':post,
#         'comment':comment,
#         'comment_form':user_comment,
#         'cate':cat,
#         'is_liked':is_liked,
#         'total_likes':post.total_likes()
#     }
#     return render(request, 'blog/login_read_post.html', content)