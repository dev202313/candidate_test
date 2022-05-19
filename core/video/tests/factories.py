from __future__ import annotations

import factory
from django.contrib.auth.models import User
from faker import Faker

from video.models import Post

fake = Faker(["en", "fr", "ar"])


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.last_name()
    password = fake.password(length=8)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    is_staff = False
    is_superuser = False
    is_active = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title_fr = fake.bs()
    title_ar = fake.bs()
    title_en = fake.bs()
    extract_fr = fake.text(max_nb_chars=200)
    extract_ar = fake.text(max_nb_chars=200)
    extract_en = fake.text(max_nb_chars=200)
    content_fr = fake.text(max_nb_chars=1000)
    content_ar = fake.text(max_nb_chars=1000)
    content_en = fake.text(max_nb_chars=1000)
    status = "PB"
