from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from blog.blog_form import SignUp, CompleteProfileForm, PostForm, EditProfile, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post, Category, Comments
from django.http import Http404

# Create your views here.


# view for blog homepage
def blog(request):
    category = Category.objects.all() 
    blog_post = Post.objects.all().order_by('-time')
    args = {'post':blog_post, 'cate':category}
    return render (request, 'blog/blog.html', args)

# view for read_more page
def post_read(request, pos_id):
    try:
        pol = Post.objects.get(id=pos_id)
        comments = Comments.objects.filter(post=pol).order_by('comment_time')
    except Post.DoesNotExist:
        Http404('The page you are accessing does not exist')
    return render(request, 'blog/read_post.html', {'post':pol, 'comments':comments})

# view for login homepage
@login_required
def blog_login(request):
    category = Category.objects.all()
    blog_post = Post.objects.all().order_by('-time')
    args = {'post':blog_post, 'cate':category, 'prof':request.user}
    return render(request, 'blog/blog_login.html', args)

# view for read_more (login) page
"""
@login_required
def login_post_read(request, pos_id):
    try:
        pol = Post.objects.get(id=pos_id)
        comments = Comments.objects.filter(post=pol).order_by('comment_time')
    except Post.DoesNotExist:
        Http404('The page you are requesting does not exist')
    return render(request, 'blog/login_read_post.html', {'post':pol, 'comments':comments})
    """

@login_required
def login_post_read(request, pos_id):
    cat = Category.objects.all()
    post = get_object_or_404(Post, id=pos_id)
    comments = Comments.objects.filter(post=post)
    if request.method == 'POST':
        user_comment = CommentForm(request.POST)
        if user_comment.is_valid():
            print(user_comment.cleaned_data)
            comment = user_comment.save(commit=False)
            comment.post = post
            comment.comment_by = request.user
            user_comment.save()
    else:
        user_comment = CommentForm()
    content = {
        'post':post,
        'comment':comments,
        'comment_form':user_comment,
        'category':cat
    }
    return render(request, 'blog/login_read_post.html', content)


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
    return render(request, 'blog/profile.html', {'prof':request.user})

# view for more user informatiom
@login_required
def complete_profile(request):
    if request.method == 'POST':
        complete = CompleteProfileForm(request.POST, request.FILES)
        if complete.is_valid():
            com_prof = complete.save(commit=False)
            com_prof.user = request.user
            complete.save()
            return redirect('blog:blog_l') 
    else:
        complete = CompleteProfileForm(request.POST, request.FILES)
    return render(request, 'blog/complete.html', {'com':complete})

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

#VIEW FOR USER'S POST
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



#views for users' comment
@login_required
def user_comment(request):
    # post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        comment2 = CommentForm(request.POST)
        if comment2.is_valid():
            print(comment2.clean_data)
            comment2.save()
    else:
        comment2 = CommentForm(request.POST)
    return render(request, 'blog/user_comment.html', {'usc':comment2})

def politics(request, pk):
    cat = Category.objects.all()
    post = Post.objects.filter(cat='politics')
    if pk:
        cat = get_object_or_404(Category, slug=pk)
        post = post.filter(cat=cat)
    comments = Comments.objects.filter(post=post)
    args = {'post':post, 'comment':comments, 'cat':cat}
    return render(request, 'blog/politics.html', args)