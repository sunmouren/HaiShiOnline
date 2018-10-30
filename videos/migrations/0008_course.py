# Generated by Django 2.1.2 on 2018-10-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20181030_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='课程名')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'ordering': ('-created',),
            },
        ),
    ]