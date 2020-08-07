from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, ButtonHolder, Div
from .models import Tasklist, Timesheet


class addTaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        exclude = ('timesheet',)
        #fields = ('timesheet_date','timesheet_created_date','is_saved')


class timesheetCreateForm(forms.ModelForm):
    timesheet_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    CHOICES = (
        ("Morning", 'Morning'),
        ("Afternoon", 'Afternoon'),
        ("Night", 'Night'),
        ("General", 'General'),
    )
    shift = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Timesheet
        fields = ('timesheet_date','shift',)

    # timesheet_date = models.DateField()
    # timesheet_created_date = models.DateField(auto_now_add=True,verbose_name='Created On')
    # is_saved =  models.BooleanField(default=False, verbose_name='Saved')
    # created_by = models.ForeignKey(User, related_name='timesheet', on_delete=models.CASCADE)
    # shift= models.CharField(max_length=255,verbose_name='Shift',default='General')

# class DateForm(forms.ModelForm):
#     timesheet_date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
#     class Meta:
#         model = Timesheet
#         fields = ('timesheet_date','shift',)




    # timesheet_date = models.DateField()
    # timesheet_created_date = models.DateField(auto_now_add=True,verbose_name='Created On')
    # is_saved =  models.BooleanField(default=False, verbose_name='Saved')
    # created_by = models.ForeignKey(User, related_name='timesheet', on_delete=models.CASCADE)

