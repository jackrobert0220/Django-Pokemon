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
    Poke("Bulbasaur", 001, "Grass"),
    Poke("Charmander", 004, "Fire"),
    Poke("Squirtle", 007, "Water"),
    Poke("Pikachu", 025, "Electric"),
]

class Poke_List(TemplateView):
    template_name = 'poke_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon'] = pokemon
        return context
