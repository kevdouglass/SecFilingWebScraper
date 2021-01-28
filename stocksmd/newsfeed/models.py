from django.db import models
from company.models import Company

# Create your models here.
class NewsArticle(models.Model):
    Company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
    Title = models.CharField(max_length=350)
    Author = models.CharField(max_length=350, blank=True)
    Release_Date = models.DateTimeField(max_length=35, blank=True)
    Year = models.CharField(max_length=25, blank=True)
    Summary= models.CharField(max_length=350, blank=True)
    Source= models.CharField(max_length=350, blank=True)
    URL = models.URLField(blank=True)
    Images = models.ImageField(upload_to='stocksmd\\newsfeed\\news', blank=True)
    Metatags = models.CharField(max_length=350, blank=True)
    
    def __str__(self):
        return self.Title
