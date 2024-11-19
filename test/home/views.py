from django.shortcuts import get_object_or_404, redirect
from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review
from django.contrib.auth.views import LoginView, LogoutView
#home page http responses defined to push data and see if the data has been pushed  
def review_form(request, movie_id=None):
    # If no movie_id is provided, redirect to the main page or return an error
    if not movie_id:
        return HttpResponse('Movie ID is required to add or view a review.', status=400)

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

            #creating review objects
            Review.objects.create(
                content_title=content_instance,  
                user=request.user,       
                rating=rating_value,
                review_description=review_description_data
            )
            
            return redirect('review_form', movie_id=movie_id)  # Redirect to prevent duplicate submissions

        else:
            return HttpResponse('You did not enter a valid review or rating. Please try again.', status=400)

    elif request.method == "GET":
        content_titles = Content.objects.values_list('title', flat=True)

        reviews = Review.objects.filter(content_title=content_instance)

        return render(request, 'review_form.html', {
            'reviews': reviews,
            'content_instance': content_instance,
        })
def view_reviews(request):
    reviews = Review.objects.all()
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
