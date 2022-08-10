from django.db import models

# Create your models here.

class Data(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True)
    date = models.DateField()
    value = models.IntegerField()
    
    def __str__(self):
        return str(self.date)
    
    