from django.shortcuts import render
from django.http import HttpResponse
from my_website_app.models import Services, Portfolio, About, Languages
from my_website_app.contact import Contact, NewsLetter #Contact2
from django.core.mail import send_mail
from my_website.settings import EMAIL_HOST_USER
from django.conf import settings
from django.contrib import messages
from django.http import Http404

# Create your views here.


def index(request):
    service_key = Services.objects.all()
    portfolio = Portfolio.objects.all()
    news = NewsLetter()
    abt = About.objects.all()
    lan = Languages.objects.all()
    form = Contact()
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['f_name']
            sender_email = form.cleaned_data['email']
            sender_comment = form.cleaned_data['comment']
            from_email = settings.EMAIL_HOST_USER
            message = '{} Has sent in a new message: {}'.format(sender_name, sender_comment)
            send_mail('Enquiry', message, sender_email, ['muyi2010@yahoo.com'])
            return HttpResponse('Message Sent')
    else:
        form = Contact()
    args = {'s_key':service_key, 'form':form, 'port':portfolio, 'nl':news, 'about':abt, 'lang':lan}
    return render(request, 'my_website_app/index.html', args)


def more(request, more_id):
    news = NewsLetter()
    try:
        serv = Services.objects.get(id = more_id)
    except Services.DoesNotExist:
        Http404('This page does not exist')
    args = {'nl':news, 'mor':serv}
    return render(request, 'my_website_app/service_more.html', args)


def about(request):
    news = NewsLetter()
    abt_me = About.objects.all()
    args = {'nl':news, 'about_m':abt_me}
    return render(request, 'my_website_app/about.html', args)

# def blog(request):
#     return render(request, 'my_website_app/blog.html')



# def contact(request):
#     form1 = Contact2()
#     if request.method == 'POST':
#         form1 = Contact2(request.POST)
#         if form1.is_valid():
#             send_name = form1.cleaned_data['f_name']
#             send_email = form1.cleaned_data['email']
#             content = form1.cleaned_data['comment']
#             message = '{} has sent you a new message: {}'.format(send_name, content)
#             send_mail('New enquiry', message, send_email, ['muyi2010@yahoo.com'])
#             return HttpResponse('Message sent! Thanks for contacting us')
#     else:
#         form1 = Contact2()
#     return render(request, 'my_website_app/contact2.html', {'form1':form1})

