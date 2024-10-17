# I (kelly) created to be imported into test cases to test //not official

##Definitions for data models

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('Movie', 'Movie'),
        ('TV Show', 'TV Show'),
    ]

    title = models.CharField(max_length=255, db_index=True)  # indexing for faster searches
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    release_year = models.PositiveIntegerField()
    maturity_rating = models.CharField(max_length=10)  # "PG-13"
    duration = models.CharField(max_length=20)  # "2h 26min" or "4 Seasons" if it's a show
    description = models.TextField()
    director = models.CharField(max_length=255)
    writers = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='content')
    languages = models.ManyToManyField(Language, related_name='content')  # supports multiple languages

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.content_type}" 

class Review(models.Model):
    content = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    rating = 
    review_description = models.CharField(max_length=1000)
    date_created  =models.CharField(max_length=255)
    
    def __str__(self):
        return

class UserProfile(models.Model):
   user =  models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   
   
   def __str__(self):
       return 


