import django_tables2 as tables
from .models import Timesheet, Tasklist
import itertools


class TimesheetTable(tables.Table):
    timesheet_date = tables.Column(linkify=("jd_tasklist", (tables.A("pk"), )))
    class Meta:
        model = Timesheet
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'id': 'table-wrapper', 'class': 'table table-hover' }
        fields = ('timesheet_date','timesheet_created_date','shift','is_saved')

class TasklistTable(tables.Table):
        class Meta:
            model = Tasklist
            template_name = 'django_tables2/bootstrap4.html'
            attrs = {'id': 'table-wrapper', 'class': 'table table-hover' }
            fields = ('assigned_by','task',)
