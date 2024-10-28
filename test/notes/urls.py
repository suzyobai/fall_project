from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', views.notes, name='notes'),
    path('view_reviews/', views.view_reviews, name='view_reviews'), #after pushing data for reviews should be able to see them here
    path('/',views.home) #added for homepage

    #path('blog/', include("blog.urls")), 
]
