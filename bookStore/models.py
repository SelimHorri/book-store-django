
from django.db import models

class Book(models.Model):
    TOPIC_CHOICES = (
        ("AVENTURE", 'Aventure'),
        ("THRILLER", 'Thriller'),
        ("FANTASTIQUE", 'Fantastique'),
        ("ROMANCE", 'Romance'),
        ("HORREUR", 'Horreur'),
        ("SCIENCEFICTION", 'cience-fiction'),
    )
    title = models.CharField(max_length=100,null=True, blank=False)
    price = models.DecimalField(max_length=100, blank=True,max_digits = 5, decimal_places = 2)
    summary = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey("GestionLivre.Author",blank=True,on_delete=models.CASCADE)
    category = models.CharField(max_length=30,choices=TOPIC_CHOICES)
    stock = models.IntegerField(blank=True,default=0)
    #TO STRING METHOD
    def __str__(self):
        return "%s" % (self.title)

class Author(models.Model):
    firstname = models.CharField(max_length=100,blank=False)
    lastname = models.CharField(max_length=100,blank=False)
    wikipedia = models.CharField(max_length=100,blank=True)
    #TO STRING METHOD
    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


