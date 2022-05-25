from __future__ import annotations

from django.test import TestCase
from django.urls import reverse

from .models import Post, User

class PostPageViewsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test-user")
        post = Post.objects.create(title="Test Post", author=user)
        self.test_page_views_slug = post.slug

    def test_page_views(self):
        self.assert_post_db_page_views(0)
        url = reverse("video:post-detail", kwargs={'slug':self.test_page_views_slug})
        resp = self.client.get(url)
        assert resp.status_code == 200
        self.assert_post_db_page_views(1)
    
    def assert_post_db_page_views(self, page_views: int):
        post = Post.objects.get(slug=self.test_page_views_slug)
        assert post.page_views == page_views
