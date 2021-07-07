from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    lang_id = models.IntegerField()
    chat_id = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'user'
        managed = False
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'

class Category(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    parent = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name_uz}'

    class Meta:
        db_table = 'category'
        managed = False
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description_uz = models.TextField(null=False, blank=False)
    description_ru = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.name_uz}'

    class Meta:
        db_table = 'product'
        managed = False
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'







