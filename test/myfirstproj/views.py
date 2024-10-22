from django.shortcuts import render, redirect
from django.http import HttpResponse
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
def myfirstproj(request):
    return HttpResponse('Hello  World!')
   # return render(request, 'home/main.html')