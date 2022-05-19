from __future__ import annotations

import pytest


# Reproducible
@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return 12345


# Settings
@pytest.fixture(autouse=True)
def use_test_settings(settings):
    settings.DEBUG = False
    settings.PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
