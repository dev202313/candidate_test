from __future__ import annotations

from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.forms import AuthenticationForm
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext
from image_cropping import ImageCroppingMixin
from import_export.admin import ImportExportModelAdmin

from . import models


class PostAdmin(ImageCroppingMixin, ImportExportModelAdmin):
    list_display = ["title_en", "author", "page_views", "date_posted"]
    exclude = ["status"]
    filter_horizontal = ("tags",)
    search_fields = ["title_en", "title_fr", "title_ar"]
    group_fieldsets = True
    fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "cover_photo",
                    "cropping",
                    "tags",
                ],
            },
        ),
        (
            _("Content - English"),
            {"fields": ["title_en", "extract_en", "content_en"], "classes": ["wide"]},
        ),
        (
            _("Content - French"),
            {"fields": ["title_fr", "extract_fr", "content_fr"], "classes": ["wide"]},
        ),
        (
            _("Content - Arabic"),
            {"fields": ["title_ar", "extract_ar", "content_ar"], "classes": ["wide"]},
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.slug = slugify(obj.title_fr)
        super().save_model(request, obj, form, change)

    @admin.action(description=_("Mark posts as published."))
    def make_published(self, request, queryset):
        updated = queryset.update(status="PB")
        self.message_user(
            request,
            ngettext(
                "%d post has been successfully marked as published.",
                "%d posts have been successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description=_("Mark posts as draft."))
    def make_draft(self, request, queryset):
        updated = queryset.update(status="DR")
        self.message_user(
            request,
            ngettext(
                "%d post has been successfully marked as draft.",
                "%d posts have been successfully marked as draft.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(models.Post, PostAdmin)
