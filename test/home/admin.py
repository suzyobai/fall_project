from django.contrib import admin

# Register your models here.
from .models import Review, Content, Genre, Language
# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Review)
admin.site.register(Content)
