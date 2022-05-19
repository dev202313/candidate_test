# Generated by Django 4.0.4 on 2022-05-18 11:25
from __future__ import annotations

import ckeditor.fields
import django.db.models.deletion
import image_cropping.fields
import taggit.managers
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('cover_photo', models.ImageField(blank=True, upload_to='uploaded_images', verbose_name='Cover Photo')),
                ('cropping', image_cropping.fields.ImageRatioField('cover_photo', '500x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Image cropping')),
                ('extract', models.TextField(blank=True, help_text='Small extract of your video', max_length=200, null=True, verbose_name='Extract')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contact')),
                ('date_posted', models.DateTimeField(auto_now=True, verbose_name='Date published')),
                ('last_modified', models.DateTimeField(auto_now_add=True, verbose_name='Last modified')),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='PB', max_length=10, verbose_name='Post status')),
                ('page_views', models.IntegerField(blank=True, default=0, editable=False, verbose_name='Page views')),
                ('author', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Blog post',
                'verbose_name_plural': 'Blog posts',
                'ordering': ('-date_posted',),
            },
        ),
    ]