from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect #Responses
from django.views.generic.base import TemplateView
from .models import Poke, PokeMove
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
#Auth imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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



@method_decorator(login_required, name='dispatch')
class Poke_Create(CreateView):
    model = Poke
    fields = ['name', 'img', 'number', 'type', 'user', 'pokemoves']
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

@method_decorator(login_required, name='dispatch')
class Poke_Update(UpdateView):
    model = Poke
    fields = ['name', 'img', 'number', 'type', 'pokemoves']
    template_name = "poke_update.html"
    #OLD success redirect
    # success_url = "/pokemon"
    #NEW success redirect
    def get_success_url(self):
        return reverse('poke_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Poke_Delete(DeleteView):
    model = Poke
    template_name = "poke_delete_confirmation.html"
    success_url = "/pokemon/"

#Profile for the User
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    pokemon = Poke.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'pokemon': pokemon})

#PokeMoves view functions
def pokemoves_index(request):
    pokemoves = PokeMove.objects.all()
    return render(request, 'pokemove_index.html', {'pokemoves': pokemoves})

def pokemoves_show(request, pokemove_id):
    pokemove = PokeMove.objects.get(id=pokemove_id)
    return render(request, 'pokemove_show.html', {'pokemove': pokemove})

@method_decorator(login_required, name='dispatch')
class PokeMove_Create(CreateView):
    model = PokeMove
    fields = '__all__'
    template_name = "pokemove_form.html"
    success_url = '/pokemoves'

@method_decorator(login_required, name='dispatch')
class PokeMove_Update(UpdateView):
    model = PokeMove
    fields = ['name', 'type']
    template_name = "pokemove_update.html"
    success_url = '/pokemoves'

@method_decorator(login_required, name='dispatch')
class PokeMove_Delete(DeleteView):
    model = PokeMove
    template_name = "pokemove_confirm_delete.html"
    success_url = '/pokemoves'

#Login, Logout, and Signup
def login_view(request):
    # if POST, then authenticate the user (submit the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled')
                    # Feel free to redirect them somewhere 
            else:
                print('The username and/or password is incorrect')
    else:
        #user is going to the login page
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/pokemon')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hey', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try again...</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})