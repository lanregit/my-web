from django import forms
from django.core import validators
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from blog.models import CompleteUser_Profile, Post, Comment_user





# REGISTER FORM
class SignUp(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Choose a Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password again'}))

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            
        return user

#MODEL FORM FOR MORE USER INFORMATION
class CompleteProfileForm(forms.ModelForm):
    class Meta():
        Male = 'ml'
        Female = 'fm'
        Gender =[
            (Male,'male'),
            (Female, 'female')
        ]
        model = CompleteUser_Profile
        exclude = ('user', 'time')
        widgets = {
            'gender': forms.RadioSelect(choices=Gender),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Phone No'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'placeholder':'About Me'}),
            'dob': forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
            'profile_pic': forms.ClearableFileInput() 
        }

        fields = ['gender', 'phone', 'location', 'dob', 'profile_pic', 'bio']

    

# EDIT PROFILE FORM 

class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        exclude = ('username', 'email')
        widgets = {
            'first_name':forms.TimeInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'})
        }
    # class Meta:
    #     model = CompleteProfileForm
    #     fields = ['phone', 'location', 'dob', 'profile_pic', 'bio']
    #     exclude = ('gender',)
    #     widgets = {
    #         'phone':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Phone Number'}),
    #         'loction':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Location'}),
    #         'dob':forms.DateInput(attrs={'class':'form-control', 'Placeholder':'YYYY-MM-DD'}),
    #         'bio':forms.Textarea(attrs={'class':'form-control', 'Placeholder':'About Me'}),
    #         'phone':forms.ClearableFileInput(attrs={'class':'form-control', 'Placeholder':'Phone Number'}),
    #     }

# USERS' POST FORM
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content', 'img', 'cat'}
        exclude = ('time',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Post Content'}),
            'img':forms.ClearableFileInput()
        }
        
    
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content', 'img', 'cat'}
        exclude = ('time',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Post Content'}),
            'img':forms.ClearableFileInput()
        }
        
    
#USERS' COMMENT FORM
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_user
        fields ={'comment',}
        exclude = ('comment_time',)
        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control', 'placeholder':' Write Your Comment'})
        }

# USERS' REPLY FORM
# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields ={'reply',}
#         exclude = ('reply_time',)
#         widgets = {
#             'reply':forms.Textarea(attrs={'class':'form-control', 'placeholder':' Write Your Comment'})
#         }

