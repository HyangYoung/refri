from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string


class User(AbstractUser):
    class DietChoices(models.TextChoices):
        VEGAN = "V", "Vegan"
        HALAL = "H", "Halal"
        KOSHER = "K", "Kosher"
        GLUTENFREE  = "G", "Gluten Free"

    bio = models.TextField(blank=True)
    diet = models.CharField(max_length=4, blank=True, choices=DietChoices.choices)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="Please upload 48px * 48px size file")

