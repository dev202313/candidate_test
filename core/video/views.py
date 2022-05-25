from __future__ import annotations

from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    """Returns list of all posts."""
    
    # see Post.Meta for ordering
    posts=Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "post_list.html", context)


def post_detail(request: HttpRequest, slug:str) -> HttpResponse:
    """Returns post detail page."""

    try:
        post=Post.objects.get(slug=slug)
        post.page_views += 1
        post.save()
    except Post.DoesNotExist:
        return HttpResponseNotFound(_("This element does not exist."))

    context = {
        "post": post,
    }

    return render(request, "post_detail.html", context)
