from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

class ToolInput(EmbeddedDocument):
	movie_name = fields.StringField(required=True)
    imdb_rating = fields.DynamicField(required=True)

# Create your models here.
