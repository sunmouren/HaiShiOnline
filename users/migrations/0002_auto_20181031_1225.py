# Generated by Django 2.1.2 on 2018-10-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='image/default.jpg', upload_to='image/user/avatar', verbose_name='头像'),
        ),
    ]
