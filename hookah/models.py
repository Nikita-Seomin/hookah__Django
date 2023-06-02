from django.db import models


# Create your models here.

class Schedule(models.Model):
    day = models.CharField(max_length=255, verbose_name="День")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    time_open = models.TimeField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Время открытия")
    time_close = models.TimeField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Время закрытия")
    is_open = models.BooleanField(default=True, verbose_name="Открыто или нет")

    def __str__(self):
        return self.day


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=30, blank=True, verbose_name="Номер телефона")
    login = models.CharField(max_length=60, blank=True, verbose_name="Логин")
    password = models.CharField(max_length=60, verbose_name="Пароль")
    e_mail = models.CharField(max_length=60, blank=True, verbose_name="E-mail")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Цена")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    count = models.DecimalField(max_digits=10, decimal_places=0, blank=True, verbose_name="Колличество")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")


class Chat(models.Model):
    message = models.TextField(blank=True, verbose_name="Сообщение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    user = models.ForeignKey('Users', on_delete=models.PROTECT, null=True, verbose_name="Пользователь")
