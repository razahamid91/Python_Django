from django.db import models

# Create your models here.

class Booking(models.Model):
    DESTINATION_CHOICES =(('India','India'),('Paris','Paris'),('NewYork','NewYork'),('TOKIA','TOKIA'))
    destinations = models.CharField(max_length=100, choices=DESTINATION_CHOICES)
    full_name= models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    adults=models.IntegerField(default=1)
    children=models.IntegerField(default=0)
    special_request=models.TextField()
    
    

    
