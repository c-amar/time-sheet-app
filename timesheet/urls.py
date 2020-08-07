"""jd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timesheet_app import views as timesheet_views
from account import views as accounts_views
from django.conf.urls import include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

#####timesheet######
    path('timesheet/', timesheet_views.jd_timesheet, name='jd_timesheet'),
    path('timesheet/addtimesheet', timesheet_views.timesheetAddView, name='timesheetAddView'),
    #path('timesheet/tasklist/(?P<pk>\d+)/', timesheet_views.jd_tasklist, name='jd_tasklist'),
    path('timesheet/(?P<pk>\d+)/', timesheet_views.jd_tasklist, name='jd_tasklist'),
    path('timesheet/(?P<pk>\d+)/addtask', timesheet_views.addTaskView, name='addTaskView'),
    path('timesheet/(?P<pk>\d+)/addtask/save', timesheet_views.saveView, name='saveView'),
    path('timesheet/report', timesheet_views.reportView, name='reportView'),


#####account#########
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]