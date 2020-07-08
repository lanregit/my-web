# Generated by Django 2.1 on 2019-12-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website_app', '0003_auto_20191222_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Project Image')),
                ('p_title', models.CharField(max_length=150, verbose_name='Project Title')),
                ('p_describe', models.TextField(verbose_name='Project Description')),
                ('role', models.CharField(max_length=150, verbose_name='Role Played')),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='img',
        ),
    ]