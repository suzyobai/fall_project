from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review, Content
#import pyrebase
from collections import OrderedDict #ordered dictionary to maintain order of data inputed into the databse

"""
#firebase config for the project
config = {
  "apiKey": "AIzaSyBIHJD2lpVnA2PCrMsRVQyXgrgs6Znd450",
  "authDomain": "nesrksite.firebaseapp.com",
  "databaseURL": "https://nesrksite-default-rtdb.firebaseio.com",
  "projectId": "nesrksite",
  "storageBucket": "nesrksite.appspot.com",
  "messagingSenderId": "987473157973",
  "appId": "1:987473157973:web:4434c5d89ff62ab54499dc",
  "measurementId": "G-EFS66P0MS5"
};
#initialize firebase with config
firebase = pyrebase.initialize_app(config)
db = firebase.database() #get a refrence to the firebase realtime database

def home(request): 
    #fetching data from the fruitsall child node in the dball parent node
    getdata = db.child("dball").child("fruitsall").get()
    odict = OrderedDict(getdata.val())
    return render(request, "main.html", {"data":odict})
def add(request):
    #get fruits feild value from the inputted data
    if request.method == "POST":
        fruits = request.POST['fruits']
        #push new fruit data to the firebase database under dball/fruitsall
        result = db.child("dball").child("fruitsall").push({"name" : fruits}) 
    #redirect to blog page once fruit is added 
    return redirect("/blog")
"""
"""
def myfirstproj(request):
    
    if request.method == "POST": #posting data into db
        if request.POST['content'] and request.POST['rating']:
            content=request.POST['content']
            #create a new review using Review.objects.create()
            #add to db with the save method
            return HttpResponse('Review Successfully added to database', status=200) #added a status code to pass testcase 
        else:
            return HttpResponse('You did not enter a valid review or rating, please try again',status=400)
    else:
        return HttpResponse("Write your review here", status=200) 
    #200 means worked sucessfully, 302 is page gets redirected, 400 is when invalid data/inputs r given        
"""

# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Content, Review
from django.contrib.auth.views import LoginView 

def myfirstproj(request):
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
    return render(request, 'view_reviews.html', {'reviews': reviews})

def home(request): #placeholder for homepage to display all the movie pngs and stars
    return HttpResponse('Welcome', status=200)

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'