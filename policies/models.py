from django.db import models
from django.conf import settings

from tariffs.models import Tariff


class AccidentPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="инн", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Територия страхования")
    insured_elsewhere = models.BooleanField(default=False)

    def __str__(self):
        return self.policy_num


class CarPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="инн", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    user_is_owner = models.BooleanField(default=True, verbose_name="Страховщик владелец")
    insured_elsewhere = models.BooleanField(default=False)
    car_mark = models.CharField(max_length=255, verbose_name="Марка машины")
    car_model = models.CharField(max_length=255, verbose_name="Модель машины")
    car_date_release = models.CharField(max_length=255)
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Територия страхования")
    type_control = models.CharField(max_length=255, choices=("default", "under attorney", "all"))

    def __str__(self):
        return self.policy_num


class CargoPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="инн", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
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
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")

    def __str__(self):
        return self.policy_num


class VZRPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="инн", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    place = models.CharField(max_length=255, choices=("Шенген", "Турция", "США"))
    travelGoal = models.CharField(max_length=255, choices=(
        "Деловая поездка", "Туризм", "Гостевая", "Частная", "Спорт", "Воссоединение семьи", "Лечение", "Учеба",
        "Стажировка"))

    def __str__(self):
        return self.policy_num


class DMSPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="инн", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    date_beginning = models.DateField(verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания полиса")
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)

    def __str__(self):
        return self.policy_num
