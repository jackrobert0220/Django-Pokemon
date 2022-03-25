from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Poke
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Poke_List(TemplateView):
    template_name = 'pokelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #gets name query to access it
        name = self.request.GET.get("name")
        #if query exists, will filter by name
        if name != None:
            context["pokemon"] = Poke.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else: 
            context['pokemon'] = Poke.objects.all() # this is where we add the key into our context object for the view to use
            context['header'] = "Our Pokemon"
        return context

class PokeCreate(CreateView):
    model = Poke
    fields = ['name', 'img', 'number', 'type']
    template_name = "poke_create.html"
    success_url = "/pokemon/"

class PokeDetail(DetailView):
    model = Poke
    template_name = "poke_detail.html"
