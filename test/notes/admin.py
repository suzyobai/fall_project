from django.contrib import admin
from .models import Review, Content, Genre, Language
# Register your models here.
admin.site.register(Review)
admin.site.register(Content)
admin.site.register(Genre)
admin.site.register(Language)