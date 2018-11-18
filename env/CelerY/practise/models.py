from django.db import models

# Create your models here.
class Info(models.Model):
    Username = models.CharField(max_length = 100)
    Organisation = models.CharField(max_length = 50 , blank = True)
    date_visit = models.DateField()
    def __str__(self):
        return '{} {}'.format(self.Username,self.date_visit)
