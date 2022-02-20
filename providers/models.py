from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf.global_settings import LANGUAGES
from static.currencies import CURRENCIES


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)
    language = models.CharField(choices=LANGUAGES, max_length=8, blank=False, default='en')
    currency = models.CharField(choices=CURRENCIES, max_length=8, blank=False, default='USD')

    def __str__(self):
        return 'Provider Name: {}'.format(self.name)
