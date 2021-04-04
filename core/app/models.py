from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Расширяем модель пользователя для добавления дополнительной информации,
    фактически создаем объект SocialAccount allauth с дополнительной информацией.
    """
    extra_data = models.CharField('Дополнительные данные в расширенной модели', max_length=512)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'