# Generated by Django 2.1 on 2020-10-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200929_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeuser_profile',
            name='gender',
            field=models.CharField(choices=[('ML', 'male'), ('FM', 'female')], default='ML', max_length=2, null=True),
        ),
    ]