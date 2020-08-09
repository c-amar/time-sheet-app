from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Timesheet, Tasklist


from django.template.loader import render_to_string
from .tables import TimesheetTable, TasklistTable
from .forms import addTaskForm, timesheetCreateForm
from django_tables2 import RequestConfig
from django.http import JsonResponse
from django.http import HttpRequest
from django.db.models import Q
from django_tables2.export.export import TableExport
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def reportView(request):
    timesheet = Timesheet.objects.all()
    tasklist = Tasklist.objects.all()
    return render(request, 'report.html', {'timesheet': timesheet, 'tasklist': tasklist})

@login_required
def jd_timesheet(request):

    login_user = request.user
    #TimesheetTable.objects.filter(created_by=login_user)
    #table_timesheet = TimesheetTable(Timesheet.objects.all())
    table_timesheet = TimesheetTable(Timesheet.objects.filter(created_by=login_user))
    return render(request, 'timesheet.html', {'table_timesheet': table_timesheet})

@login_required
def timesheetAddView(request):
    data = dict()
    #timesheet = get_object_or_404(Timesheet, pk=pk)
    if request.method == 'POST':
        form = timesheetCreateForm(request.POST)
        login_user = request.user
        print(form.is_valid)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.created_by = login_user
            timesheet.save()
            return redirect('jd_timesheet')
    else:
        form = timesheetCreateForm()

    data['html_form'] = render_to_string('addTimesheet_partial.html', {'form': form,}, request=request)
    return JsonResponse(data)


@login_required
def jd_tasklist(request, pk):

    timesheet1 = Timesheet.objects.get(pk=pk)
    table_tasklist = TasklistTable(Tasklist.objects.filter(timesheet=pk))
    return render(request, 'timesheet_tasklist.html', {'table_tasklist': table_tasklist, 'timesheet1': timesheet1})


@login_required
def saveView(request, pk):
    timesheet = Timesheet.objects.get(pk=pk)
    if not timesheet.is_saved:
        timesheet.is_saved = True
        timesheet.save()
    return redirect('jd_tasklist', pk=timesheet.pk)


@login_required
def addTaskView(request, pk):
    data = dict()
    timesheet = get_object_or_404(Timesheet, pk=pk)
    if request.method == 'POST':
        form = addTaskForm(request.POST)
        login_user = request.user
        if form.is_valid():
            task = form.save(commit=False)
            task.timesheet = timesheet
            task.save()
            return redirect('jd_tasklist', pk=timesheet.pk)
    else:
        form = addTaskForm()

    data['html_form'] = render_to_string('addTask_partial.html', {'form': form, 'timesheet': timesheet}, request=request)
    return JsonResponse(data)
