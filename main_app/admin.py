from django.contrib import admin
from .models import Poke # import the Cat model from models.py
# Register your models here.

admin.site.register(Poke) # this line will add the model to the admin panel