from __future__ import annotations

import pytest
from django.template.defaultfilters import slugify
from factory.base import FactoryMetaClass

from video.models import Post


@pytest.mark.django_db
def test_post_create(post_factory: FactoryMetaClass):
    """Test posts can be created"""
    post_factory.create()
    count = Post.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_post_str(example_post: Post):
    """Test post string method correct"""
    assert example_post.__str__() is example_post.title


@pytest.mark.django_db
def test_post_slug(example_post: Post):
    """Test post slug correct"""
    assert example_post.slug == slugify(example_post.title)
