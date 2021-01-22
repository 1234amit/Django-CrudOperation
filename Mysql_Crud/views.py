from django.shortcuts import render
from .models import *
from Mysql_Crud import forms
from django.db.models import Avg
# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    context={'title':"Home Page", 'musician_list':musician_list}
    return render(request,'Crud/index.html',context)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name')
    artist_reating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    context={'title':"List of the album", 'artist_info': artist_info, 'album_list':album_list,
    'artist_reating':artist_reating }
    return render(request, 'Crud/album_list.html', context)

def musician_form(request):
    form = forms.MusicianFrom()

    if request.method == 'POST':
        form = forms.MusicianFrom(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    context={'title':"Add Musician", 'musician_form':form}
    return render(request, 'Crud/musician_form.html', context)

def album_form(request):
    form = forms.AlbumFrom()

    if request.method == 'POST':
        form = forms.AlbumFrom(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    context = {'title':"Add album", 'album_form':form}
    return render(request, 'Crud/album_form.html', context)

def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianFrom(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianFrom(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    context = {'edit_form':form}
    return render(request, 'Crud/edit_artist.html',context)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumFrom(instance=album_info)
    if request.method == 'POST':
        form = forms.AlbumFrom(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
    diction = {'edit_form':form}
    diction.update({'album_id':album_id})
    return render(request, 'Crud/edit_album.html', context=diction)

def delete(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success':'Album Deleted Successfully!','album':album}
    return render(request, 'Crud/delete.html',context=diction)

def delete_musician(request, artist_id):
    artist = Musician.objects.get(id=artist_id).delete(0)
    diction = {'delete_success':'Musician Deleted Successfully!', 'artist':artist}
    return render(request,'Crud/delete.html', context=diction)

def about(request):
    context = {}
    return render(request, 'Crud/about.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        ins = Contact(name=name, address=address, contact=contact, email=email)
        ins.save()
    context = {}
    return render(request, 'Crud/contact.html',context)