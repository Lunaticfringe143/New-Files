from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class toDO(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
