from django.db import models
from fontawesome_5.fields import IconField


# Create your models here.

class Services(models.Model):
    icon = IconField(verbose_name='Font Awesome')
    title = models.CharField(max_length=100, verbose_name='Service')
    description = models.TextField(verbose_name='Service Description')
    detail = models.TextField(verbose_name='Service Detail', null=True)

    def __str__ (self):
        return self.title

class Portfolio(models.Model):
    p_image = models.ImageField(null=True, verbose_name='Project Image', blank=True, upload_to='images')
    p_title = models.CharField(max_length=150, verbose_name='Project Title')
    p_describe = models.TextField(verbose_name='Project Description')
    role = models.CharField(verbose_name='Role Played', max_length=150)
    site = models.URLField(verbose_name='Site Address', null=True)

    def __str__(self):
        return self.p_title


class About(models.Model):
    abt_img = models.ImageField(null=True, blank=True, upload_to='images', verbose_name='About Image')
    abt_content = models.TextField(verbose_name='About Summary')
    abt_detail = models.TextField(verbose_name='About Detail', null=True)

    def __str__(self):
        return self.abt_content


class Languages(models.Model):
    lan = models.CharField(verbose_name='Your Programming Languages/Tools', max_length= 100)
    l_icon = IconField(verbose_name="Icon Field")

    def __str__(self):
        return self.lan

    
