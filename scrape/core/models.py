from django.db import models
from mongoengine import Document, fields
import datetime


class Movie(Document):
    name = fields.StringField(required=True)
    actors = fields.ListField(fields.StringField(max_length=30))
    categories = fields.ListField(fields.StringField(max_length=30))
    url = fields.URLField()
    score = fields.FloatField()
    cover = fields.StringField()
    duration = fields.IntField()
    country = fields.StringField()
    released_at = fields.DateField()
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    updated_at = fields.DateTimeField(default=datetime.datetime.now)
