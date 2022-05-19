from __future__ import annotations

from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "extract",
        "content",
    )
    required_languages = ("en",)

translator.register(Post, PostTranslationOptions)
