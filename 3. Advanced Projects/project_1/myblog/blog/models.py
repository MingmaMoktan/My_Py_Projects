from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)
    
    def _str_(self):
        return self.value