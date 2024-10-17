# I (kelly) created to be imported into test cases to test //not official
# Spandana Andhavarapu: added User,SignIn, and SignUp models 
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

#User model 
class User(models.Model):
    first_name = models.CharField(max_length=255)  
    last_name = models.CharField(max_length=255)   
    email = models.EmailField(unique=True)         
    password = models.CharField(max_length=255)    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

#SignUp model to track user registrations
class SignUp(models.Model):
    #links sign up to the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    # storing the date signed-up 
    date_signed_up = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return f"SignUp for {self.user.email}"

#SignIn model
class SignIn(models.Model):
    #user email as an id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    #store password
    password = models.CharField(max_length=255)                  
    #sign in time if desired
    date_signed_in = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return f"SignIn for {self.user_id.email} on {self.date_signed_in}

