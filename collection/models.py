from django.db import models
import string

class Collection(models.Model):
    #collection_id = models.CharField(max_length=30, unique=True, primary_key=True) #No de registro
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, default="", unique=True)
    description = models.CharField(max_length=200, default="", unique=False)

    def __str__(self):
        return self.name