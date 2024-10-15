from django.shortcuts import render, redirect
def home(request): 
    return render(request, "main.html")
def add(request):
    return redirect("/blog")
