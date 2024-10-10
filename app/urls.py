from django.urls import path, include
from app.views import user_create, user_update, user_delete, user_list

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', user_create, name='user_create'),
    path('update/<int:pk>', user_update, name='user_update'),
    path('delete/<int:pk>', user_delete, name='user_delete')
]

