from __future__ import annotations

import pytest
from django.test import Client
from django.urls import reverse
from django.urls.base import resolve
from pytest_django.asserts import assertTemplateUsed
from django.http import HttpResponseNotFound

from video import views
from video.models import Post

client = Client()

@pytest.mark.django_db
def test_video_list_route():
    """tests the blog urls and views route correctly"""
    post_list_url = reverse("video:post-list")
    response = client.get(post_list_url)
    assert resolve(post_list_url).func == views.post_list
    assertTemplateUsed(response, "post_list.html")

@pytest.mark.django_db
def test_video_detail_route(example_post: Post):
    post_detail_url = reverse("video:post-detail", args=[example_post.slug])
    assert example_post.get_absolute_url() == post_detail_url

    response = client.get(post_detail_url)
    assert resolve(post_detail_url).func == views.post_detail
    assertTemplateUsed(response, "post_detail.html")


@pytest.mark.django_db
def test_video_detail_route_missing_post(example_post: Post):
    post_detail_url = reverse("video:post-detail", args=['non-existent-slug'])
    response = client.get(post_detail_url)
    assert response.status_code == 404 