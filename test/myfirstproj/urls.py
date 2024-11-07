from django.contrib import admin
from django.urls import path, include  # Import include for including app URLs
from django.conf import settings
from django.conf.urls.static import static
from myfirstproj import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('home.urls')),  # Include all URLs from the `home` app
    path('login/', views.LoginInterfaceView.as_view(), name='login'),  # Login route
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
