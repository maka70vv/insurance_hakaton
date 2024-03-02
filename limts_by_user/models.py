from django.db import models

from limits.models import Limit
from users.models import User


class LimitsByUser(models.Model):
    limit = models.ForeignKey(Limit, on_delete=models.CASCADE)
    limitName = models.CharField(max_length=100)
    summ = models.IntegerField(default=0)
    policy_num = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
