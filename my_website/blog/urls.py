from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog2'),
    path('news/<int:pos_id>/', views.post_read, name='read_post'),
    path('sign_up/', views.register, name='register'),
    path('user_profile/', views.complete_profile, name='c_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='log_in'),
    path('user-login/', views.blog_login, name='blog_l'),
    path('read/<int:pos_id>/', views.login_post_read, name='login_read_post'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('my_profile/', views.my_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user_profile/', views.complete, name='complete'),
    path('create_post/', views.user_post, name='post'),
    # path('comment/', views.user_comment, name='comment'),
    path('category/<cats>/', views.category, name='category'),
    path('<int:id>/update/', views.updatepost, name='updatepost'),    
    path('post/<int:id>/delete/', views.delete_post, name='deletepost'),    
    path('post/delete/<int:id>/confirm', views.confirm_post, name='confirmpost'),    
    path('profile/<username>/', views.userprofile, name='userprofile'),
    path('likes/', views.like_post, name='likes'),
    path('comment_likes/', views.comment_like, name='comment_like'),
    path('update_comment/<int:id>', views.updatecomment, name='update_c'),
    path('delete_comment/<int:id>', views.delete_comment, name='delete_c'),
    path('comment/<int:id>/delete', views.confirm_comment, name='confirm_delete_c'),

]