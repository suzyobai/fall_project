from django.shortcuts import render

from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review
from django.contrib.auth.views import LoginView, LogoutView
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
        # Fetch all Content titles for the dropdown
        content_titles = Content.objects.values_list('title', flat=True)

        # Get selected content_title from query parameters, if available
        selected_content_title = request.GET.get('content_title')
        
        # Fetch reviews associated with the selected content title, if provided
        reviews = []
        if selected_content_title:
            try:
                content_instance = Content.objects.get(title=selected_content_title)
                reviews = Review.objects.filter(content_title=content_instance)
            except Content.DoesNotExist:
                reviews = []  # No reviews if the content does not exist

        return render(request, 'review_form.html', {
            'content_titles': content_titles,
            'reviews': reviews,
            'selected_content_title': selected_content_title
        })

#testing to view the reviews submitted in page above^
def view_reviews(request):
    reviews = Review.objects.all()
    #print(f"Number of reviews: {reviews.count()}")
    return render(request, 'view_reviews.html', {'reviews': reviews})

def review_form(request):
    return render()


def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')
#def home(request): #placeholder for homepage to display all the movie pngs and stars
 #   return HttpResponse('Welcome', status=200)
