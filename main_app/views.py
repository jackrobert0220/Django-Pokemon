from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Poke:

    def __init__(self, name, number, kind):
        self.name = name
        self.number = number
        self.type = kind

pokemon = [
    Poke("Bulbasaur", 1, "Grass"),
    Poke("Charmander", 4, "Fire"),
    Poke("Squirtle", 7, "Water"),
    Poke("Pikachu", 25, "Electric"),
]

class Poke_List(TemplateView):
    template_name = 'pokelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon'] = pokemon
        return context
