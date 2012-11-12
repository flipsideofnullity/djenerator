from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',    
    url(r'^$', TemplateView.as_view(template_name='employee/employee_base.html'), name='employee-base'),
    url(r'^employee/$', EmployeeListView.as_view(), name='employee-list'),
    url(r'^employee/create/$', EmployeeCreateView.as_view(), name='employee-create'),
    url(r'^employee/update/(?P<pk>[0-9]+)/$', EmployeeUpdateView.as_view(), name='employee-update'),
    url(r'^employee/detail/(?P<pk>[0-9]+)/$', EmployeeDetailView.as_view(), name='employee-detail'),
    url(r'^employee/delete/(?P<pk>[0-9]+)/$', EmployeeDeleteView.as_view(), name='employee-delete'), 
)


