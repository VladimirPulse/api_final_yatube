"""Модуль для регистрации приложения api."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс регистрации приложения api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
