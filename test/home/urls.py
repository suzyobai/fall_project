from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/<int:movie_id>/', views.review_form, name='review_form'),
   #path('', views.main, name='main'),  # define the home page to view all movies on this site
    path('review_form', views.review_form, name='review_form'),
    path('home/', views.home, name='home'),
    path('view_reviews/', views.view_reviews, name='view_reviews'),  # Pushes the data for reviews 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign-up/', views.signup, name='sign-up'),
    # path('blog/', include("blog.urls")),  # Uncomment if adding blog app
]

    #path('/',views.home) #added for homepage

    #path('blog/', include("blog.urls")), 
# urls.py (usually the main project urls.py, not home/urls.py)


# Only serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
