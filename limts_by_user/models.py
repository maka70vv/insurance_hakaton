from django.db import models

from limits.models import Limit
from users.models import User


class LimtsByUser(models.Model):
    limit = models.ForeignKey(Limit, on_delete=models.CASCADE)
    summ = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
