from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компании")
    inn = models.CharField(max_length=14, verbose_name="ИНН")
    description = models.TextField(verbose_name="О компании")
    logo = models.ImageField(upload_to='companies/logo', verbose_name="Логотип компании")
    email = models.EmailField(verbose_name="Email")
    integration_url_policy = models.URLField(verbose_name="Адрес для добавления полисов")
    integration_url_customers = models.URLField(verbose_name="Адрес для добавления клиентов", null=True, blank=True)

    def __str__(self):
        return self.name
