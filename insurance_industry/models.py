from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
