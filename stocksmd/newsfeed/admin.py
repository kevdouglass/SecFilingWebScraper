from django.contrib import admin

# Register your models here.
from newsfeed.models import NewsArticle

admin.site.register(NewsArticle)