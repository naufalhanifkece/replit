from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('add/', views.add, name='books.add'),
    path('save/', views.save, name='books.save'),
    path('update/<int:book_id>/', views.update, name='books.update'),
    path('edit/<int:book_id>/', views.edit, name='books.edit'),
    path('delete/<int:book_id>/', views.delete, name='books.delete'),

]

