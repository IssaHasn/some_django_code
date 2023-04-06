from django.contrib import admin
from .models import Book, Type, Users_data

admin.site.register(Book)
admin.site.register(Type)
admin.site.register(Users_data)