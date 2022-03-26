from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect #Responses
from django.views.generic.base import TemplateView
from .models import Poke
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User

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

class Poke_Create(CreateView):
    model = Poke
    fields = ['name', 'img', 'number', 'type', 'user']
    template_name = "poke_create.html"
    #OLD create sucess redirect
    # success_url = "/pokemon/"
    #NEW create success redirect
    # def get_success_url(self):
    #     return reverse('poke_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/pokemon')

class Poke_Detail(DetailView):
    model = Poke
    template_name = "poke_detail.html"

class Poke_Update(UpdateView):
    model = Poke
    fields = ['name', 'img', 'number', 'type']
    template_name = "poke_update.html"
    #OLD success redirect
    # success_url = "/pokemon"
    #NEW success redirect
    def get_success_url(self):
        return reverse('poke_detail', kwargs={'pk': self.object.pk})

class Poke_Delete(DeleteView):
    model = Poke
    template_name = "poke_delete_confirmation.html"
    success_url = "/cats/"

#Profile for the User
def profile(request, username):
    user = User.objects.get(username=username)
    pokemon = Poke.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'pokemon': pokemon})