from django.contrib import admin
from .models import Poke, PokeMove # import the Cat model from models.py
# Register your models here.

admin.site.register(Poke) # this line will add the model to the admin panel
admin.site.register(PokeMove)