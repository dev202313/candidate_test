"""Uses factories to create model instances used in tests_*.py"""
from __future__ import annotations

import pytest
from django.contrib.auth.models import User
from factories import PostFactory
from factories import UserFactory
from factory.base import FactoryMetaClass
from pytest_factoryboy import register

from video import models

register(PostFactory)
register(UserFactory)

@pytest.fixture
def example_user(db, user_factory: FactoryMetaClass) -> User:
    """Creates an example user and saves to test db"""
    user = user_factory.create()
    return user

@pytest.fixture
def example_post(db, post_factory: FactoryMetaClass) -> models.Post:
    """Creates an example post and saves to test db"""
    post = post_factory.create()
    return post
