# Generated by Django 4.0 on 2022-03-11 06:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contract', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('bio', models.CharField(blank=True, default='No bio.......', max_length=50, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('banner_img', models.ImageField(upload_to='posts', validators=[django.core.validators.FileExtensionValidator])),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog.profile')),
                ('liked', models.ManyToManyField(blank=True, related_name='likes', to='blog.Profile')),
            ],
        ),
    ]
