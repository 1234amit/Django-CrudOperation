from django import forms
from Mysql_Crud import models

class MusicianFrom(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumFrom(forms.ModelForm):
    relese_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"