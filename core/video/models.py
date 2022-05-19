from __future__ import annotations

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from image_cropping import ImageRatioField
from taggit.managers import TaggableManager

# Choices for post status:
DRAFT = "DR"
PUBLISHED = "PB"
options = (
    (DRAFT, _("Draft")),
    (PUBLISHED, _("Published")),
)

class Post(models.Model):
    """A blog post object."""

    title = models.CharField(verbose_name=_("Title"), max_length=150, unique=True)
    slug = SlugField(_("Slug"), unique=True, blank=True, null=True)
    cover_photo = models.ImageField(
        verbose_name=_("Cover Photo") ,blank=True, upload_to="uploaded_images"
    )
    cropping = ImageRatioField(
        verbose_name=_("Image cropping"), image_field="cover_photo", size="500x500"
    )
    extract = models.TextField(
        verbose_name=_("Extract"),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("Small extract of your video"),
    )
    content = RichTextField(verbose_name=_("Contact"), blank=True, null=True)
    date_posted = models.DateTimeField(verbose_name=_("Date published"), auto_now=True)
    last_modified = models.DateTimeField(verbose_name=_("Last modified"), auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, editable=False, related_name="posts", verbose_name=('Author')
    )
    tags = TaggableManager(blank=True)
    status = models.CharField(
        _("Post status"), max_length=10, choices=options, default="PB"
    )
    page_views = models.IntegerField(default=0, editable=False, verbose_name=_("Page views"), blank=True)

    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blog posts")
        ordering = ("-date_posted",)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title_en

    def get_absolute_url(self) -> str:
        return reverse("video:post-detail", kwargs={"slug": self.slug})
