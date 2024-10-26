# Create your tests here.
import json
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import Content, Genre, Language, Review
from django.contrib.auth.models import User

# User/SignUp test cases
class UserModelTest(TestCase):
    def setUp(self):
        # User instance creation
        self.user = User.objects.create_user(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            username="john@example.com",
            password="supersecurepassword123",  # Password is hashed automatically
        )

    def test_user_creation(self):
        # Test that user object is created correctly
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john@example.com")

    def test_user_str_representation(self):
        # Test the __str__ method of the User model
        self.assertEqual(str(self.user), "john@example.com") #change to email 

# Review test cases
class ReviewFeatureTest(TestCase):
    def setUp(self):
        # Create user and content (movie) instances
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.movie = Content.objects.create(title='Test Movie', description='A great movie!', release_year=2010)
        self.tangled =  Content.objects.create(
            title="Tangled",
            content_type="Movie",  # Movie or TV Show
            release_year=2010,
            maturity_rating="PG",  # Example: "PG"
            duration="1h 40min",  # Example format
            description="The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.",
            director="Nathan Greno, Byron Howard",
            writers="Dan Fogelman, Jacob Grimm, Wilhelm Grimm",
            stars="Mandy Moore, Zachary Levi, Donna Murphy"
        )


    def test_review_prompt_box_appears(self):
        # Test that the review prompt box appears when accessing the review page
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/myfirstproj/')
        self.assertContains(response, 'Write your review here') 
        self.assertContains(response, 'Rating')
        self.assertContains(response, self.movie.description)

    def test_successful_review_submission(self): #error here ValueError: Field 'id' expected a number but got 'Amazing movie!'.
        # Test that a review is successfully saved with valid input
        #create a content instance that has the title Tangled already in 
        #run the test on that
        
            #sending a post request with the inputed data
        self.client.login(username='testuser', password='password123')
        response = self.client.post('/myfirstproj/', {
            'content_title' : self.tangled.title,
            'content': 'Amazing movie!',
            'rating': 5
        })
        #if post send data 

        self.assertEqual(response.status_code, 200)  # Assuming a redirect occurs after posting
        self.assertTrue(Review.objects.filter(content_title=self.tangled, content="Amazing movie!", rating=5).exists()) #checking if content is in db
        
        #user=self.user
        #content = respoonse.content

    def test_view_reviews_on_movie_page(self):
    # Test that reviews are displayed on the movie page
        review_content = Content.objects.create(
            title='Deadpool',
            description='Amazing movie with great storytelling!',
            release_year=2023  # Use any valid release year
        )
        
        review = Review.objects.create(
            #movie=self.movie,           # Assign the Content instance for the movie
            content_title=self.movie, #change to self.content? prob use review_content
            user=self.user,            # Assign the User instance
            rating=5,                  # Assign the rating
            review_description=review_content      # Assign the Content instance to content field
        )
        
        response = self.client.get('/myfirstproj/')  # Corrected typo from '/myirstproj/'
        print(response)
        self.assertContains(response, review.content.description)  # Check if review content is in the response
        self.assertContains(response, f"{review.rating} stars")  # Check for the rating display
"""
# Search test cases
class SearchTestCase(TestCase):
    def setUp(self):
        self.action_genre = Genre.objects.create(name="Action")
        self.drama_genre = Genre.objects.create(name="Drama")
        self.english_language = Language.objects.create(name="English")
        self.spanish_language = Language.objects.create(name="Spanish")

        self.content1 = Content.objects.create(
            title="The Hunger Games: Catching Fire",
            release_year=2013,
            description="Katniss Everdeen and Peeta Mellark become targets of the Capitol after their victory in the 74th Hunger Games sparks a rebellion in the Districts of Panem."
        )
        self.content1.genres.add(self.action_genre)

        self.content2 = Content.objects.create(
            title="La Casa de Papel",
            content_type="TV Show",
            description="Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan"
        )
        self.content2.genres.add(self.drama_genre)

    def test_search_genre(self):
        results = Content.objects.filter(genres=self.action_genre)
        self.assertTrue(results.exists())
        self.assertEqual(results.first().title, "The Hunger Games: Catching Fire")

    def test_search_language(self):
        results = Content.objects.filter(language=self.spanish_language)
        self.assertTrue(results.exists())
        self.assertEqual(results.first().title, "La Casa de Papel")

    def test_search_by_genre_and_language(self):
        results = Content.objects.filter(genres=self.drama_genre, language=self.spanish_language)
        self.assertTrue(results.exists())
        self.assertEqual(results.first().title, "La Casa de Papel")

class HomepageTestCase(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = Client()
        self.homepage_url = '/myfirstproj/'  # Directly use the URL path

        # Set up sample data for movies
        self.movie = Content.objects.create(
            title="Sample Movie",
            content_type="Movie",
            release_year=2021,
            description="A sample movie for testing."
        )

    def test_homepage_loads_successfully(self):
        # Test that the homepage loads and returns a 200 status code
        response = self.client.get(self.homepage_url)
        self.assertEqual(response.status_code, 200, "Homepage did not load successfully")

    def test_movie_list_is_displayed(self):
        # Test that the homepage contains a list of movies with ratings
        response = self.client.get(self.homepage_url)
        self.assertContains(response, self.movie.title)
        self.assertContains(response, 'rating-overview')  # Adjust based on actual HTML structure

    def test_search_bar_is_present(self):
        # Test that the search bar is present on the homepage
        response = self.client.get(self.homepage_url)
        self.assertContains(response, '<input type="text" name="search"', html=True)

    def test_hamburger_button_is_present(self):
        # Test that the hamburger menu button is present on the homepage
        response = self.client.get(self.homepage_url)
        self.assertContains(response, 'class="hamburger-button"', html=True)  # Adjust based on actual HTML ID/class
"""