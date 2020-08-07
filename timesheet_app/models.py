from django.db import models

# Create your models here.

from simple_history.models import HistoricalRecords

from django.contrib.auth.models import User


class Timesheet(models.Model):

    timesheet_date = models.DateField()
    timesheet_created_date = models.DateField(auto_now_add=True,verbose_name='Created On')
    is_saved =  models.BooleanField(default=False, verbose_name='Saved')
    created_by = models.ForeignKey(User, related_name='timesheet', on_delete=models.CASCADE)
    shift= models.CharField(max_length=255,verbose_name='Shift',default='General')
    class Meta:
        unique_together = ('timesheet_date', 'created_by',)
    
    def __str__(self):
        return self.created_by

class Tasklist(models.Model):

   task =  models.TextField(max_length=1000, verbose_name='Task')
   assigned_by = models.CharField(max_length=255, verbose_name='Assigned By')
   timesheet = models.ForeignKey(Timesheet,related_name='tasklist', on_delete=models.CASCADE)

   def __str__(self):
       return self.task
   
