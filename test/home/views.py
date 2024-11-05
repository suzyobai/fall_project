from django.shortcuts import render

from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review

#home page http responses defined to push data and see if the data has been pushed  
def home(request):
    if request.method == "POST":
        if 'content_title' in request.POST and 'review_description' in request.POST and 'rating' in request.POST:
            content_title_data = request.POST['content_title']
            review_description_data = request.POST['review_description']
            rating_data = request.POST['rating']
            
            try:
                rating_value = int(rating_data)
                if not (1 <= rating_value <= 5):
                    return HttpResponse('Invalid rating value. Rating must be between 1 and 5.', status=400)
            except ValueError:
                return HttpResponse('Rating must be a number.', status=400)

            try:
                content_instance = Content.objects.get(title=content_title_data)

                Review.objects.create(
                    content_title=content_instance,  
                    user=request.user,       
                    rating=rating_value,
                    review_description=review_description_data
                )
                
                return HttpResponse('Review successfully added to database.', status=200)
            except Content.DoesNotExist:
                return HttpResponse('Content not found.', status=400)
        else:
            return HttpResponse('You did not enter a valid review or rating. Please try again.', status=400)

    elif request.method == "GET":
        return render(request, 'review_form.html')

#view_reviews http responses defined to view all reviews on a page
def view_reviews(request):
    reviews = Review.objects.all()
    #print(f"Number of reviews: {reviews.count()}")
    return render(request, 'view_reviews.html', {'reviews': reviews})

#def home(request): #placeholder for homepage to display all the movie pngs and stars
 #   return HttpResponse('Welcome', status=200)