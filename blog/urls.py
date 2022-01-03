from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='articles_list'),    
    path('create/', views.create, name='create_article'),
    path('edit/<int:id>/', views.edit, name='edit_article'),
    path('<int:id>/delete', views.delete, name='delete_article'),
    path('search/', views.search_posts, name='search_posts'),
    path('<slug:slug>/', views.show, name='show_article'),
] 