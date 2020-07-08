# Generated by Django 2.1 on 2020-02-20 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Post Title')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='picture')),
                ('content', models.TextField(verbose_name='Post')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cat', models.ManyToManyField(to='blog.Category', verbose_name='Select Post Category')),
                ('poster', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Post By')),
            ],
        ),
    ]
