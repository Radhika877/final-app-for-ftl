import uuid
from django.db import models

# Create your models here.
class user(models.Model):
    
    id = models.CharField(max_length=100, null=False, blank=False, unique=True,primary_key=True)
    real_name = models.CharField(max_length=30,null=False)
    tz = models.CharField(max_length=20,null=False)
    
    class Meta:
        db_table = 'user'
        
class activity_periods(models.Model):
    start_time = models.DateTimeField(auto_now_add=True,null=False)
    end_time = models.DateTimeField(auto_now=True,null=False)
    
    class Meta:
        db_table='activity_periods'

    def __str__(self):
        return self.order_id
        