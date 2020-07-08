from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog2'),
    path('news/<int:pos_id>/', views.post_read, name='read_post'),
    path('sign_up/', views.register, name='register'),
    path('user_profile2/', views.complete_profile, name='c_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='log_in'),
    path('user-login/', views.blog_login, name='blog_l'),
    path('news2/<int:pos_id>/', views.login_post_read, name='login_read_post'),
    path('', auth_views.LogoutView.as_view, name='logout'),
    path('profile/', views.my_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user_profile/', views.complete, name='complete'),
    path('create_post/', views.user_post, name='post'),
    path('comment/', views.user_comment, name='comment'),
    path('politics/', views.politics, name='politics'),
]