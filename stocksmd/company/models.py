from django.db import models

# Create your models here.
class Company(models.Model):
    Ticker = models.CharField(max_length=5, blank=True)
    Name = models.CharField(max_length=250, blank=True)
    Logo = models.ImageField(upload_to='news', blank=True)
    ISIN = models.CharField(max_length=50, blank=True)
    CUSIP = models.CharField(max_length=50, blank=True)
    CIK = models.CharField(max_length=50, blank=True)
    Industry = models.CharField(max_length=250, blank=True)
    Ceo = models.CharField(max_length=350, blank=True)
    Institutional_Owners = models.CharField(max_length=10, blank=True)
    Shares_Outstanding = models.CharField(max_length=50, blank=True)
    Institutional_Shares = models.CharField(max_length=100, blank=True)
    Institutional_Value = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.Ticker + ' - ' + self.Name 
    
    