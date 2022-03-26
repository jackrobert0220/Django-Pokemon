from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES = (
    ("e", "electric"),
    ("d", "dragon"),
    ("f", "fire"),
    ("g", "ghost"),
    ("n", "normal"),
    ("p", "plant"),
    ("ps", "psychic"),
    ("r", "rock"),
    ("w", "water"),
)


class PokeMove(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices = TYPE_CHOICES)

    def __str__(self):
        return self.name

TYPE_CHOICES = (
    ("e", "electric"),
    ("d", "dragon"),
    ("f", "fire"),
    ("g", "ghost"),
    ("n", "normal"),
    ("p", "plant"),
    ("ps", "psychic"),
    ("r", "rock"),
    ("w", "water"),
)


class Poke(models.Model):

    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    number = models.IntegerField()
    type = models.CharField(max_length=10, choices = TYPE_CHOICES)
    #USER implementation
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 1:M example
    pokemoves = models.ManyToManyField(PokeMove) # M:M example

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
            ordering = ['name']


