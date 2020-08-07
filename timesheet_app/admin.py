from django.contrib import admin

from .models import Timesheet, Tasklist

# Register your models here.


admin.site.register(Timesheet)
admin.site.register(Tasklist)
