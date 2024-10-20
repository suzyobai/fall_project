'''
Notes for me (;
git add .
git commit -m 
git push origin main
'''
# Create your tests here.

#edited by kelly not offically pushed yet
#edited by spandana: User, SignIn, SignUp testcases added and pushed

# tests.py
from django.test import TestCase, reverse
from .models import Content, Genre, Language, Review, User, SignIn, SignUp
from django.contrib.auth.models import User

#User/SignIn/SignUp testcases
class UserModelTest(TestCase):
    def setUp(self):
        #user instance
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            password="supersecurepassword123",  # Note: In production, password should be hashed
        )

    def test_user_creation(self):
        #testing user object is created correctly
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john@example.com")

    def test_user_str_representation(self):
        #testing he __str__ method of the User model
        self.assertEqual(str(self.user), "John Doe (john@example.com)")

class SignUpModelTest(TestCase):
    def setUp(self):
        #creating user instance for the signup
        self.user = User.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            password="securepassword456",  # Use hashing in production
        )

        #creating a SignUp instance
        self.signup = SignUp.objects.create(
            user=self.user
        )

    def test_signup_creation(self):
        #testing the signup object is created correctly
        self.assertEqual(self.signup.user, self.user)
        self.assertIsNotNone(self.signup.date_signed_up)  # Check if the date is auto-set

    def test_signup_str_representation(self):
        #testing __str__ method of the SignUp model
        self.assertEqual(str(self.signup), f"SignUp for {self.user.email}")

class SignInModelTest(TestCase):
    def setUp(self):
        #creating a user instance for sign-in
        self.user = User.objects.create(
            first_name="Alice",
            last_name="Johnson",
            email="alice@example.com",
            password="anotherpassword789",  # Use hashing in production
        )

        #creating a SignIn instance
        self.signin = SignIn.objects.create(
            user_id=self.user,
            password="anotherpassword789"  # Use proper validation in production
        )

    def test_signin_creation(self):
        #testing if the signin object is created correctly
        self.assertEqual(self.signin.user_id, self.user)
        self.assertEqual(self.signin.password, "anotherpassword789")
        self.assertIsNotNone(self.signin.date_signed_in)  # Check if the date is auto-set

    def test_signin_str_representation(self):
        #testing the __str__ method of the SignIn model
        self.assertEqual(str(self.signin), f"SignIn for {self.user.email} on {self.signin.date_signed_in}")

# Review test cases
class ReviewFeatureTest(TestCase):
    def setUp(self):
        # Creating user and content (movie) instances
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.movie = Content.objects.create(title='Test Movie', description='A great movie!', poster='test_poster.jpg')

    # Test that the review prompt box appears when a user accesses the review page.
    def test_review_prompt_box_appears(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(f'/movies/{self.movie.id}/review/')
        self.assertContains(response, 'Write your review here')
        self.assertContains(response, 'Rating')
        self.assertContains(response, self.movie.description)
        self.assertContains(response, self.movie.poster.url)

    # Test that a review is successfully saved when valid input is provided.
    def test_successful_review_submission(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(f'/movies/{self.movie.id}/review/', {
            'content': 'Amazing movie!',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect occurs after posting
        self.assertTrue(Review.objects.filter(movie=self.movie, user=self.user).exists())

    # Test that reviews are displayed on the movie page.
    def test_view_reviews_on_movie_page(self):
        Review.objects.create(movie=self.movie, user=self.user, content='Amazing!', rating=5)
        response = self.client.get(f'/movies/{self.movie.id}/')
        self.assertContains(response, 'Amazing!')
        self.assertContains(response, '5 stars')
        
        
class SearchTestCase(TestCase):
    def setUp(self):
        
        self.action_genre = Genre.objects.create(name="Action")
        self.drama_genre = Genre.objects.create(name="Drama")
        self.english_language = Language.objects.create(name="English")
        self.spanish_language = Language.objects.create(name="Spanish")

        self.content1 = Content.objects.create(
            title="The Hunger Games: Catching Fire",
            release_year=2013,
            content_type="Movie",
            description="Katniss Everdeen and Peeta Mellark become targets of the Capitol after their victory in the 74th Hunger Games sparks a rebellion in the Districts of Panem.",
            language=self.english_language
        )
        self.content1.genres.add(self.action_genre)

        self.content2 = Content.objects.create(
            title="La Casa de Papel",
            release_year=2017,
            content_type="TV Show",
            description="Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan",
            language=self.spanish_language
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
    def setUp(self):
        # Initialize the test client
        self.client = Client()
        # Replace 'homepage' with the actual name of the URL pattern for the homepage
        self.homepage_url = reverse('homepage')  # Ensure this matches your urls.py

        # Set up sample data for movies
        self.movie = Content.objects.create(
            title="Sample Movie",
            content_type="Movie",
            release_year=2021,
            maturity_rating="PG-13",
            duration="2h",
            description="A sample movie for testing.",
            director="Sample Director",
            writers="Sample Writer",
            stars="Sample Star",
        )
class HomepageTestCase(TestCase): 
    def setUp(self):
        # Initialize the test client
        self.client = Client()
        self.homepage_url = reverse('blog')  #change it to match a page from urls.py page after making a page

        # Set up sample data for movies
        self.movie = Content.objects.create(
            title="Sample Movie",
            content_type="Movie",
            release_year=2021,
            maturity_rating="PG-13",
            duration="2h",
            description="A sample movie for testing.",
            director="Sample Director",
            writers="Sample Writer",
            stars="Sample Star",
        )

    def test_homepage_loads_successfully(self):
        """
        Test that the homepage loads and returns a 200 status code.
        """
        response = self.client.get(self.homepage_url)
        self.assertEqual(response.status_code, 200, "Homepage did not load successfully")

    def test_movie_list_is_displayed(self):
        """
        Test that the homepage contains a list of movies with ratings.
        """
        response = self.client.get(self.homepage_url)
        # Check for the presence of movie title and rating overview
        self.assertContains(response, self.movie.title)
        self.assertContains(response, 'rating-overview')  # adjust based on actual HTML structure

    def test_search_bar_is_present(self):
        """
        Test that the search bar is present on the homepage.
        """
        response = self.client.get(self.homepage_url)
        # Check for search bar input (assuming 'search' is the name of the input field)
        self.assertContains(response, '<input type="text" name="search"', html=True)

    def test_hamburger_button_is_present(self):
        """
        Test that the hamburger menu button is present on the homepage.
        """
        response = self.client.get(self.homepage_url)
        # Check for hamburger button (replace 'hamburger-button' with the actual HTML ID/class)
        self.assertContains(response, 'class="hamburger-button"', html=True)  # Adjust based on actual HTML ID/class