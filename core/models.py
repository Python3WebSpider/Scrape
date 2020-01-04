from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, Model, URLField, FloatField, IntegerField, DateField, DateTimeField

class Movie(Model):
    name = CharField(max_length=255)
    actors = ArrayField(CharField(max_length=255, null=True, blank=True), null=True, blank=True)
    categories = ArrayField(CharField(max_length=255, null=True, blank=True), null=True, blank=True)
    url = URLField(null=True, blank=True)
    score = FloatField(null=True, blank=True)
    cover = CharField(max_length=255, null=True, blank=True)
    duration = IntegerField(null=True, blank=True)
    country = CharField(max_length=255, null=True, blank=True)
    released_at = DateField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
