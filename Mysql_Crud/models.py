from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relese_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent!")
    )
    num_stars = models.IntegerField(choices=rating)
    def __str__(self):
        return self.name + "," + str(self.num_stars)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

