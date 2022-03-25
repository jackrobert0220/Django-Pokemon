from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('pokemon/', views.Poke_List.as_view(), name="poke_list"),
    path('about/', views.About.as_view(), name="about"),
    path('pokemon/new/', views.PokeCreate.as_view(), name="poke_create"),
    path('pokemon/<int:pk>/', views.PokeDetail.as_view(), name="poke_detail"),
    path('pokemon/<int:pk>/update', views.PokeUpdate.as_view(), name="poke_update")
]