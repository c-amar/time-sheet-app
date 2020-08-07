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



#    task =  models.TextField(max_length=1000, verbose_name='Task')
#    assigned_by = models.CharField(max_length=255, verbose_name='Assigned By')
#    timesheet = models.ForeignKey(Timesheet,related_name='tasklist', on_delete=models.CASCADE)           

#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page


# def creatView(request):
    
#     data = dict()
#     #global search_query

#     #if 'search_query' not in request_query.GET:
#     #    search_query = 'NULL'

#     if request.method == 'POST':
#         a = jdInventoryViews.objects.get(view_name="default")
#         form = InventoryViewForm(request.POST, instance=a)
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             inactiveTuple = viewFilter()
#             table_global.exclude = inactiveTuple
#             #table = InventoryTable(jdInventory.objects.filter(Q(ip_addr__icontains=search_query) | Q(hw_serialno__icontains=search_query) | Q(virtual_ip__icontains=search_query)))
#             #table.exclude = inactiveTuple
#             RequestConfig(request, paginate={'per_page': 20}).configure(table_global)
#             data['html_book_list'] = render_to_string('jd_inventory_partial.html', {'table': table_global}, request=request_query)
#         else:
#             data['form_is_valid'] = False
#     else:
#         a = jdInventoryViews.objects.get(view_name="default")
#         form = InventoryViewForm(instance=a)


#     context = {'form': form}
#     data['html_form'] = render_to_string('partial_view_create.html',
#         context,
#         request=request,
#     )
#     return JsonResponse(data)


# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})


