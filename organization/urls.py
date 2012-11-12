from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',    
    url(r'^$', TemplateView.as_view(template_name='organization/organization_base.html'), name='organization-base'),
    url(r'^organization/$', OrganizationListView.as_view(), name='organization-list'),
    url(r'^organization/create/$', OrganizationCreateView.as_view(), name='organization-create'),
    url(r'^organization/update/(?P<pk>[0-9]+)/$', OrganizationUpdateView.as_view(), name='organization-update'),
    url(r'^organization/detail/(?P<pk>[0-9]+)/$', OrganizationDetailView.as_view(), name='organization-detail'),
    url(r'^organization/delete/(?P<pk>[0-9]+)/$', OrganizationDeleteView.as_view(), name='organization-delete'),
    url(r'^department/$', DepartmentListView.as_view(), name='department-list'),
    url(r'^department/create/$', DepartmentCreateView.as_view(), name='department-create'),
    url(r'^department/update/(?P<pk>[0-9]+)/$', DepartmentUpdateView.as_view(), name='department-update'),
    url(r'^department/detail/(?P<pk>[0-9]+)/$', DepartmentDetailView.as_view(), name='department-detail'),
    url(r'^department/delete/(?P<pk>[0-9]+)/$', DepartmentDeleteView.as_view(), name='department-delete'), 
)


