from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=40)
