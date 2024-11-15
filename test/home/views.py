from django.shortcuts import get_object_or_404, render

from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review
from django.contrib.auth.views import LoginView, LogoutView
#home page http responses defined to push data and see if the data has been pushed  
def review_form(request, movie_id=None):
    # Fetch the movie (Content) instance by its ID
    content_instance = get_object_or_404(Content, id=movie_id)
    
    if request.method == "POST":
        if 'review_description' in request.POST and 'rating' in request.POST:
            review_description_data = request.POST['review_description']
            rating_data = request.POST['rating']
            
            try:
                rating_value = int(rating_data)
                if not (1 <= rating_value <= 5):
                    return HttpResponse('Invalid rating value. Rating must be between 1 and 5.', status=400)
            except ValueError:
                return HttpResponse('Rating must be a number.', status=400)

            # Create the review associated with the selected Content
            Review.objects.create(
                content_title=content_instance,  
                user=request.user,       
                rating=rating_value,
                review_description=review_description_data
            )
            
            return HttpResponse('Review successfully added to database.', status=200)

        else:
            return HttpResponse('You did not enter a valid review or rating. Please try again.', status=400)

    elif request.method == "GET":
        # Fetch all Content titles for the dropdown (if needed elsewhere)
        content_titles = Content.objects.values_list('title', flat=True)

        # Fetch reviews associated with the selected content (movie)
        reviews = Review.objects.filter(content_title=content_instance)

        return render(request, 'review_form.html', {
            'content_titles': content_titles,  # Optional, for a dropdown if needed
            'reviews': reviews,
            'selected_content_title': content_instance.title,
        })#testing to view the reviews submitted in page above^
def view_reviews(request):
    reviews = Review.objects.all()
    #print(f"Number of reviews: {reviews.count()}")
    return render(request, 'view_reviews.html', {'reviews': reviews})

def main(request):
    movies = Content.objects.all()  # Fetch all Content objects
    return render(request, 'main.html', {'movies': movies})


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')
#def home(request): #placeholder for homepage to display all the movie pngs and stars
 #   return HttpResponse('Welcome', status=200)
