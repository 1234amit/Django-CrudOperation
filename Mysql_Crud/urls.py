from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('add_album/', views.album_form, name="add_album"),
    path('add_musician/', views.musician_form, name="add_musician"),
    path('album_list/<int:artist_id>/', views.album_list, name="album_list"),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name="edit_artist"),
    path('edit_album/<int:album_id>/', views.edit_album, name="edit_album"),
    path('delete/<int:album_id>/', views.delete, name="delete"),
    path('delete_musician/<int:artist_id>/', views.delete_musician, name="delete_musician"),
]