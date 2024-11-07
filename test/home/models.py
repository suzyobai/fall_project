from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

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

    image = models.ImageField(upload_to='content_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.content_type}"

class Review(models.Model):
    rating = models.PositiveIntegerField()
    review_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='app_reviews')  # Adjusted related_name
    content_title = models.ForeignKey(Content, on_delete=models.CASCADE) #updated foreign key 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content_title.title} - {self.rating}/5"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='app_userprofile')  # Adjusted related_name
    email = models.EmailField()

    def __str__(self):
        return self.user.username

