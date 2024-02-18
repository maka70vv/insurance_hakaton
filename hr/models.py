from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Jobs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')
    responsibilities = models.TextField(verbose_name='Обязанности')

    def __str__(self):
        return self.title


class Workers(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО сотрудника')
    corp_email = models.EmailField(verbose_name='Корпоративный email', null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    inn = models.CharField(max_length=14, verbose_name='ИНН', unique=True)
    passport = models.CharField(max_length=30, verbose_name='Серия и номер паспорта')
    job = models.ManyToManyField(Jobs, verbose_name='Должность')
    salary = models.PositiveIntegerField(verbose_name='Зарплата (на руки)')
    employmentDate = models.DateField(verbose_name='Дата принятия на работу')
    dismissalDate = models.DateField(verbose_name='Дата увольнения')
    active = models.BooleanField(default=True, verbose_name='Активный сотрудник')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Аккаунт в системе', null=True, blank=True)
    cv = models.FileField(verbose_name='Резюме', upload_to='CVs', null=True, blank=True)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=Workers)
def link_worker_to_user(sender, instance, created, **kwargs):
    if created:
        try:
            user_with_same_inn = User.objects.get(workers__inn=instance.inn)
            instance.user = user_with_same_inn
            instance.save()
        except User.DoesNotExist:
            pass