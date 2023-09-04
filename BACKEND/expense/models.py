from django.db import models

# Create your models here.
class expense(models.Model):
    expid=models.BigAutoField(primary_key=True)
    datetime=models.DateTimeField(auto_now_add=True)
    crnt_bal=models.IntegerField(default=0)
    difference=models.IntegerField(default=0)
    reason=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.crnt_bal)
