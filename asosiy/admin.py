from django.contrib import admin
from .models import News
from modeltranslation.admin import TranslationAdmin

@admin.register(News)
class ProductAdmin(TranslationAdmin):
    list_display = ("sarlavha",'rasm', 'matn', 'sana', 'korishlar_soni')

