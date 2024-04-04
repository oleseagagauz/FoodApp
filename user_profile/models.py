from datetime import date
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    SCOPE_CHOICES = [
        ('weight_loss', 'Сброс веса'),
        ('maintenance', 'Поддержание формы'),
        ('muscle_gain', 'Набор мышечной массы'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        (1.2, 'Минимальные движения, работа сидя, передвижение на автомобиле, отсутствие дополнительных физических '
              'нагрузок'),
        (1.3, 'Небольшая двигательная нагрузка, необходимость каждый день много передвигаться пешком или 1-2 '
              'раза/неделю бег трусцой, езда на велосипеде, командные спортивные игры, легкий физический труд'),
        (1.5, 'Посещение фитнес-клуба 3-5 раз в неделю, активный физический труд'),
        (1.7, 'Высокая физическая активность, регулярный тяжелый физический труд или ежедневные продолжительные '
              'занятия спортом'),
        (1.9, 'Очень высокий уровень физической активности. Обычно в таком режиме живут спортсмены '
              'перед соревнованиями')
    ]

    MALE = 1
    FEMALE = 2

    SEX_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]

    sex = models.IntegerField(choices=SEX_CHOICES)
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES)
    activity_level = models.FloatField(choices=ACTIVITY_LEVEL_CHOICES, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    weight = models.FloatField()
    height = models.FloatField()
    birthdate = models.DateField()
    age = models.IntegerField(null=True)
    creation_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate age based on birthdate
        if self.birthdate:
            today = date.today()
            age = today.year - self.birthdate.year - (
                        (today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            self.age = age
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Профиль для пользователя {self.user.username}"

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class UserIMT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    value = models.FloatField()
    status = models.CharField(max_length=50)
    recommended_calories = models.IntegerField(default=0)

    def __str__(self):
        return f'ИМТ пользователя {self.user.username}'

    class Meta:
        verbose_name = 'ИМТ'
        verbose_name_plural = 'ИМТ'
