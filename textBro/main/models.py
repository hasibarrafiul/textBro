from django.db import models


class texts(models.Model):
    text_link = models.CharField(max_length=20, unique=True)
    text_password = models.CharField(max_length=100)
    text = models.TextField(default="", blank=True)
    text1 = models.TextField(default="", blank=True)
    text2 = models.TextField(default="", blank=True)
    text3 = models.TextField(default="", blank=True)
    text4 = models.TextField(default="", blank=True)
    text5 = models.TextField(default="", blank=True)
    text6 = models.TextField(default="", blank=True)
    text7 = models.TextField(default="", blank=True)
    text8 = models.TextField(default="", blank=True)
    text9 = models.TextField(default="", blank=True)
