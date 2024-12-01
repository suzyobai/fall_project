from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),  # define the home page to view all movies on this site, change to homepage
    path('review_form/<int:movie_id>/', views.review_form, name='review_form'),  #requires movie id to redirect to same page
    path('view_reviews/', views.view_reviews, name='view_reviews'),  # Pushes the data for reviews 
    path('', views.login_view, name='login_view'), #login is the inital page
    path('logout/', views.logout, name='logout'),
    path('sign-up/', views.signup, name='sign-up'),
]


# Only serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
