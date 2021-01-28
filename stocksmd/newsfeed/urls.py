from django.urls import path
from newsfeed.views import index, article_details

urlpatterns = [
     # /news/
    path('', index, name='index'),
    
    # /news/some_id#/
        # /news/712/
            # '^' = start of regex, '$' = end of regex pattern
    # path(r'^(?P<article_id>[0-9]+)/$', article_details, name='details'),
    path('<article_id>', article_details, name='article-details'),
]