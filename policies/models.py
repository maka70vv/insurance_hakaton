from django.db import models
from django.conf import settings

from insurance_companies.models import Company
from tariffs.models import Tariff

PLACE_CHOICES = (
    ('schengen', 'Шенген'),
    ('turkey', 'Турция'),
    ('usa', 'США'),
)

TRAVEL_GOAL_CHOICES = (
    ('business_trip', 'Деловая поездка'),
    ('tourism', 'Туризм'),
    ('guest', 'Гостевая'),
    ('private', 'Частная'),
    ('sports', 'Спорт'),
    ('family_reunion', 'Воссоединение семьи'),
    ('treatment', 'Лечение'),
    ('education', 'Учеба'),
    ('internship', 'Стажировка'),
)

class AccidentPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="ИНН", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Территория страхования")
    insured_elsewhere = models.BooleanField(default=False)
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Страховая компания")
    price = models.IntegerField(verbose_name="Стоимость полиса (без комиссии)")
    price_with_commission = models.IntegerField(verbose_name="Стоимость полиса с комиссией сервиса")
    commission_summ = models.IntegerField(verbose_name="Сумма комиссии")

    def __str__(self):
        return self.policy_num


class CarPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="ИНН", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    user_is_owner = models.BooleanField(default=True, verbose_name="Страховщик владелец")
    insured_elsewhere = models.BooleanField(default=False)
    car_mark = models.CharField(max_length=255, verbose_name="Марка машины")
    car_model = models.CharField(max_length=255, verbose_name="Модель машины")
    car_date_release = models.CharField(max_length=255)
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    insurance_territory = models.CharField(max_length=255, verbose_name="Территория страхования")
    type_control = models.CharField(max_length=255, choices=(
        ('default', 'По умолчанию'),
        ('under_attorney', 'По доверенности'),
        ('all', 'Все варианты'),
    ))
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Страховая компания")
    price = models.IntegerField(verbose_name="Стоимость полиса (без комиссии)")
    price_with_commission = models.IntegerField(verbose_name="Стоимость полиса с комиссией сервиса")
    commission_summ = models.IntegerField(verbose_name="Сумма комиссии")

    def __str__(self):
        return self.policy_num


class CargoPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="ИНН", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    cargo_name = models.CharField(max_length=255, verbose_name="Наименование груза")
    isnew_cargo = models.BooleanField(default=True, verbose_name="Новый груз")
    length = models.PositiveIntegerField(verbose_name="Длина")
    width = models.PositiveIntegerField(verbose_name="Ширина")
    height = models.PositiveIntegerField(verbose_name="Высота")
    cargo_volume = models.PositiveIntegerField(verbose_name="Объем")
    cargo_weight = models.PositiveIntegerField(verbose_name="Вес")
    is_fragile = models.BooleanField(default=False, verbose_name="Хрупкий груз")
    cargo_quantity_amount = models.PositiveIntegerField(verbose_name="Количество единиц груза")
    cargo_unit_amount = models.PositiveIntegerField(verbose_name="Количество грузовых мест")
    actual_price = models.PositiveIntegerField(verbose_name="Стоимость груза")
    insurance_price = models.PositiveIntegerField(verbose_name="Страховая сумма")
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Страховая компания")
    price = models.IntegerField(verbose_name="Стоимость полиса (без комиссии)")
    price_with_commission = models.IntegerField(verbose_name="Стоимость полиса с комиссией сервиса")
    commission_summ = models.IntegerField(verbose_name="Сумма комиссии")

    def __str__(self):
        return self.policy_num


class VZRPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="ИНН", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса")
    date_beginning = models.DateField(auto_now_add=True, verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания")
    place = models.CharField(max_length=255, choices=PLACE_CHOICES, verbose_name="Место")
    travelGoal = models.CharField(max_length=255, choices=TRAVEL_GOAL_CHOICES, verbose_name="Цель поездки")
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Страховая компания")
    price = models.IntegerField(verbose_name="Стоимость полиса (без комиссии)")
    price_with_commission = models.IntegerField(verbose_name="Стоимость полиса с комиссией сервиса")
    commission_summ = models.IntegerField(verbose_name="Сумма комиссии")

    def __str__(self):
        return self.policy_num


class DMSPolicy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=14, verbose_name="ИНН", null=True, blank=True)
    policy_num = models.CharField(max_length=10, unique=True, verbose_name="Номер полиса", null=True)
    date_beginning = models.DateField(verbose_name="Дата начала полиса")
    date_expiration = models.DateField(verbose_name="Дата окончания полиса")
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    insurance_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Страховая компания")
    price = models.IntegerField(verbose_name="Стоимость полиса (без комиссии)", null=True, blank=True)
    price_with_commission = models.IntegerField(verbose_name="Стоимость полиса с комиссией сервиса", null=True, blank=True)
    commission_summ = models.IntegerField(verbose_name="Сумма комиссии", null=True, blank=True)
    fam_member1_inn = models.CharField(max_length=14, verbose_name="ИНН прикрепленного члена семьи №1", null=True, blank=True)
    fam_member2_inn = models.CharField(max_length=14, verbose_name="ИНН прикрепленного члена семьи №1", null=True, blank=True)

    def __str__(self):
        return self.policy_num
