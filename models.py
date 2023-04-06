from django.db import models

class Type(models.Model):
    type_name = models.CharField(max_length = 75)
    def __str__(self):
        return self.type_name

class Book(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)
    image = models.ImageField(upload_to = 'photos/%y/%m/%d')
    type_of_id = models.ManyToManyField('Type')
    def __str__(self):
        return self.name

class Users_data(models.Model):
    user = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    shoping = models.ManyToManyField('Book', null = True, blank = True)
    def __str__(self):
        return self.user