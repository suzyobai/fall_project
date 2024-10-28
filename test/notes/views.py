from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review, Content
#import pyrebase
from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse
# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review

def notes(request):
    if request.method == "POST":
        if 'content_title' in request.POST and 'content' in request.POST and 'rating' in request.POST:
            content_title_data = request.POST['content_title']
            content_data = request.POST['content']
            rating_data = request.POST['rating']

            rating_value = int(rating_data)
            if 1 <= rating_value <= 5:
                try:
                    # Fetch the content instance by title
                    content_instance = Content.objects.get(title=content_title_data)
                    # Create the review
                    Review.objects.create(
                        title=content_instance,
                        user=request.user,
                        rating=rating_value
                    )
                    return HttpResponse('Review Successfully added to database', status=200)
                except Content.DoesNotExist:
                    return HttpResponse('Content not found.', status=400)
            else:
                return HttpResponse('Invalid rating value. Rating must be between 1 and 5.', status=400)
        else:
            return HttpResponse('You did not enter a valid review or rating, please try again', status=400)
    else:
        # Render the HTML template for the review form on a GET request
        if request.method == "GET": 
            return render(request, 'review_form.html')
def view_reviews(request):
    reviews = Review.objects.all()
    #print(f"Number of reviews: {reviews.count()}")
    return render(request, 'view_reviews.html', {'reviews': reviews})

def home(request): #placeholder for homepage to display all the movie pngs and stars
    return HttpResponse('Welcome', status=200)