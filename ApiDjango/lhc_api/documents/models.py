from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now=True)
    