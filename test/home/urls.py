from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Sets the home view as the homepage for ref.
    path('home/', views.home, name='home'),
    path('view_reviews/', views.view_reviews, name='view_reviews'),  # Pushes the data for reviews 
    #path('login/', views.LoginInterfaceView.as_view(), name='login'), #added for login
    #path('logout/', views.LogoutInterfaceView.as_view(), name='logout'), #added for logout

    # path('blog/', include("blog.urls")),  # Uncomment if adding blog app
]

    #path('/',views.home) #added for homepage

    #path('blog/', include("blog.urls")), 
