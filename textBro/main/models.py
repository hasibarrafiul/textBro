from django.db import models


class texts(models.Model):
    text_link = models.CharField(max_length=20, unique=True)
    text_password = models.CharField(max_length=20)
    text = models.TextField()
