from django.db import models
from django.core.validators import URLValidator


class URL(models.Model):
    slug = models.SlugField(unique=True)
    full_url = models.TextField(validators=[URLValidator()])
    short_url = models.URLField()
    access_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.short_url