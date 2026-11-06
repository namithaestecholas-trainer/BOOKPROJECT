from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/',views.book_create, name='book_create'),
    path('update/<int:id>/', views.book_update, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
]