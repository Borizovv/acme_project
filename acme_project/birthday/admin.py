from django.contrib import admin


# Из модуля models импортируем модель
from .models import Birthday, Tag

APP_MODELS = (Birthday, Tag)
admin.site.register(APP_MODELS)
# admin.site.register(Tag)