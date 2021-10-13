from django.urls import path
from . import views

app_name ='posts'


urlpatterns = [
    # Главная страница
    path('', views.index, name='main_page'),
    path('group/<slug:slug>/',views.group_posts, name='groups_page')
] 