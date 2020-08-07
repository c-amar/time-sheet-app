import django_tables2 as tables
from .models import Timesheet, Tasklist
import itertools


class TimesheetTable(tables.Table):
   
    #hw_serialno = tables.Column(linkify=("jd_inventory_detailed_view", (tables.A("hw_serialno"), )))
    timesheet_date = tables.Column(linkify=("jd_tasklist", (tables.A("pk"), )))
    #counter = tables.Column(empty_values=(), orderable=False, verbose_name="ID")
   # export_formats = ['csv', 'xls']
   # def render_counter(self):
   #     self.row_counter = getattr(self, 'row_counter', itertools.count(self.page.start_index()))
   #     return next(self.row_counter)  
    class Meta:
        model = Timesheet
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'id': 'table-wrapper', 'class': 'table table-hover' }
        fields = ('timesheet_date','timesheet_created_date','shift','is_saved')

        #fields = ('hw_serialno', 'location', 'st_holdername','ip_addr', 'global_category', 'main_module', 'sub_module', 'status', 'comment')
        #fields = ('counter','hw_serialno', 'location', 'st_holdername', 'ip_addr', 'global_category', 'main_module', 'sub_module', 'status', 'comment', 'hostname', 'make', 'cpu_info', 'cores', 'mem_info', 'os_info', 'os_major_version', 'kernel_info', 'wwn', 'virtual_ip', 'installed_packages', 'slave_of', 'master_of', 'ntp_cron_info', 'ntp_config_info', 'resolver', 'mail_dns', 'listen_services', 'lb_info', 'backend_cluster', 'password_expiry', 'docker_info', 'is_virtual', 'is_primary', 'is_redundant', 'services_running', 'dracip', 'blade_no', 'chasis_no')


class TasklistTable(tables.Table):
        class Meta:
            model = Tasklist
            template_name = 'django_tables2/bootstrap4.html'
            attrs = {'id': 'table-wrapper', 'class': 'table table-hover' }
            fields = ('assigned_by','task',)

# class ReportTable(tables.Table):
#     timesheet_date = tables.Column(accessor='timesheet.timesheet_date')