from django.urls import path
from my_website_app import views

app_name = 'my_web_app'

urlpatterns =[
    path('', views.about, name='about_me'),
    path('service/<int:more_id>/', views.more, name='service'),
    # path('blog/', views.blog, name='blog'),
    
    #path('contact/', views.contact, name='contact2'),
]