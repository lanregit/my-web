# Generated by Django 2.1 on 2020-07-01 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200331_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]