from django.db import models
from django.conf import settings


class AccidentPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_beginning = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateTimeField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Територия страхования")
    insured_elsewhere = models.BooleanField(default=False)


class CarPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    user_is_owner = models.BooleanField(default=True, verbose_name="Страховщик владелец")
    insured_elsewhere = models.BooleanField(default=False)
    car_mark = models.CharField(max_length=255, verbose_name="Марка машины")
    car_model = models.CharField(max_length=255, verbose_name="Модель машины")
    car_date_release = models.CharField(max_length=255)
    date_beginning = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateTimeField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Територия страхования")
    type_control = models.CharField(max_length=255, choices=("default", "under attorney", "all"))


class CargoPolicy(models.Model):
    cargo_name = models.CharField(max_length=255, verbose_name="Наименования груза")
    isnew_cargo = models.BooleanField(default=True, verbose_name="Новый груз")
    danger_class = models.CharField(max_length=255, verbose_name="Класс опасности")
    length = models.PositiveIntegerField(verbose_name="Длинна")
    width = models.PositiveIntegerField(verbose_name="Ширина")
    height = models.PositiveIntegerField(verbose_name="Высота")
    cargo_volume = models.PositiveIntegerField(verbose_name="Объем")
    cargo_weight = models.PositiveIntegerField(verbose_name="Вес")
    is_fragile = models.BooleanField(default=False, verbose_name="Хрупкие груз")
    cargo_quantity_amount = models.PositiveIntegerField(verbose_name="Количество единиц груза")
    cargo_unit_amount = models.PositiveIntegerField(verbose_name="Количество грузовых мест")
    actual_price = models.PositiveIntegerField(verbose_name="Стоиместь груза")
    insurance_price = models.PositiveIntegerField(verbose_name="Страховая сумма")
    date_beginning = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateTimeField(verbose_name="Дата окончания")
