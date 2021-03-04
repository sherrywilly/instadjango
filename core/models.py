from django.db import models
from datetime import datetime

# Create your models here.


class Customer(models.Model):
    uname = models.SlugField(primary_key=True)
    sdate = models.DateField(auto_now_add=True,blank=True,null=True)
    edate = models.DateField()

    @property
    def premium(self):
        if self.edate<=datetime.today().date():
            return False
        else:
            return True

    def __str__(self):
        return self.uname + "    "+str(self.premium)
    
            

