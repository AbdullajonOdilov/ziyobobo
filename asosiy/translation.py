from .models import News
from modeltranslation.translator import TranslationOptions, register

@register(News)
class ProductTranslationOptions(TranslationOptions):
    fields = ('sarlavha', 'matn')