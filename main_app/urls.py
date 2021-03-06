from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('pokemon/', views.Poke_List.as_view(), name="poke_list"),
    path('about/', views.About.as_view(), name="about"),
    path('pokemon/new/', views.Poke_Create.as_view(), name="poke_create"),
    path('pokemon/<int:pk>/', views.Poke_Detail.as_view(), name="poke_detail"),
    path('pokemon/<int:pk>/update', views.Poke_Update.as_view(), name="poke_update"),
    path('pokemon/<int:pk>delete', views.Poke_Delete.as_view(), name="poke_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('pokemoves/', views.pokemoves_index, name='pokemoves_index'),
    path('pokemoves/<int:pokemove_id>', views.pokemoves_show, name='pokemoves_show'),
    path('pokemoves/create/', views.PokeMove_Create.as_view(), name='pokemoves_create'),
    path('pokemoves/<int:pk>/update/', views.PokeMove_Update.as_view(), name='pokemoves_update'),
    path('pokemoves/<int:pk>/delete/', views.PokeMove_Delete.as_view(), name='pokemoves_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]