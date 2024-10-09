from django.urls import path, include
from app.views import show_name_and_surname, show_age, show_hobby

urlpatterns = [
    path('name_and_surname/', show_name_and_surname, name='name_and_surname'),
    path('show_age/', show_age, name='show_age'),
    path('show_hobby/', show_hobby, name='show_hobby')
]

