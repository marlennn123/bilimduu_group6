from modeltranslation.translator import translator, TranslationOptions, register
from .models import Car, Bet


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('name', 'category', 'city', 'country', 'color', 'description',)

