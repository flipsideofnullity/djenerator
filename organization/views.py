from django.views.generic import *
from django.db.models import Q
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from djenerator.views import *
from .models import *
from .forms import *

class DepartmentCreateView(CRUDCreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department-list')

    def get_queryset(self):
        return super(DepartmentCreateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.created_by = self.request.user
            form.instance.modified_by = self.request.user
        messages.success(self.request, _("Succesfully added!!!"))
        return super(DepartmentCreateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(DepartmentCreateView, self).get_context_data()

class DepartmentUpdateView(CRUDUpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department-list')    

    def get_queryset(self):
        return super(DepartmentUpdateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.modified_by = self.request.user
        form.instance.version += 1
        messages.success(self.request, _("Successfully updated!!!"))        
        return super(DepartmentUpdateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(DepartmentUpdateView, self).get_context_data()


class DepartmentDetailView(CRUDDetailView):
    model = Department

    def get_queryset(self):
        return super(DepartmentDetailView, self).get_queryset()
        
    def get_context_date(self):
        return super(DepartmentDetailView, self).get_context_data()
        
class DepartmentListView(CRUDListView):
    model = Department
    paginate_by = 15

    def get_queryset(self):       
        qs = super(DepartmentListView, self).get_queryset()
        query = self.request.GET.get("q", None)
        sort_type, sort_by = (self.request.GET.get("sort", None), 
            self.request.GET.get("sortby", None),)
            
        if sort_type and sort_by:
            qs = qs.order_by("{}{}".format("" if sort_type=="asc" else "-", sort_by))
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | 
                Q(remarks__icontains=query)
            )
        return qs
        
    def get_context_date(self):
        return super(DepartmentListView, self).get_context_data()
        
class DepartmentDeleteView(CRUDDeleteView):
    model = Department
    success_url = reverse_lazy('department-list')
        
    def form_valid(self, form):
        messages.success(self.request, _("Deletion complete!!!"))        
        return super(DepartmentDeleteView, self).form_valid(form)

class OrganizationCreateView(CRUDCreateView):
    model = Organization
    form_class = OrganizationForm
    success_url = reverse_lazy('organization-list')

    def get_queryset(self):
        return super(OrganizationCreateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.created_by = self.request.user
            form.instance.modified_by = self.request.user
        messages.success(self.request, _("Succesfully added!!!"))
        return super(OrganizationCreateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(OrganizationCreateView, self).get_context_data()

class OrganizationUpdateView(CRUDUpdateView):
    model = Organization
    form_class = OrganizationForm
    success_url = reverse_lazy('organization-list')    

    def get_queryset(self):
        return super(OrganizationUpdateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.modified_by = self.request.user
        form.instance.version += 1
        messages.success(self.request, _("Successfully updated!!!"))        
        return super(OrganizationUpdateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(OrganizationUpdateView, self).get_context_data()


class OrganizationDetailView(CRUDDetailView):
    model = Organization

    def get_queryset(self):
        return super(OrganizationDetailView, self).get_queryset()
        
    def get_context_date(self):
        return super(OrganizationDetailView, self).get_context_data()
        
class OrganizationListView(CRUDListView):
    model = Organization
    paginate_by = 15

    def get_queryset(self):       
        qs = super(OrganizationListView, self).get_queryset()
        query = self.request.GET.get("q", None)
        sort_type, sort_by = (self.request.GET.get("sort", None), 
            self.request.GET.get("sortby", None),)
            
        if sort_type and sort_by:
            qs = qs.order_by("{}{}".format("" if sort_type=="asc" else "-", sort_by))
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | 
                Q(remarks__icontains=query)
            )
        return qs
        
    def get_context_date(self):
        return super(OrganizationListView, self).get_context_data()
        
class OrganizationDeleteView(CRUDDeleteView):
    model = Organization
    success_url = reverse_lazy('organization-list')
        
    def form_valid(self, form):
        messages.success(self.request, _("Deletion complete!!!"))        
        return super(OrganizationDeleteView, self).form_valid(form)

