from django.views.generic import *
from django.db.models import Q
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from djenerator.views import *
from .models import *
from .forms import *

class EmployeeCreateView(CRUDCreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def get_queryset(self):
        return super(EmployeeCreateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.created_by = self.request.user
            form.instance.modified_by = self.request.user
        messages.success(self.request, _("Succesfully added!!!"))
        return super(EmployeeCreateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(EmployeeCreateView, self).get_context_data()

class EmployeeUpdateView(CRUDUpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')    

    def get_queryset(self):
        return super(EmployeeUpdateView, self).get_queryset()
    
    def form_valid(self, form):
        if not self.request.user.is_anonymous():
            form.instance.modified_by = self.request.user
        form.instance.version += 1
        messages.success(self.request, _("Successfully updated!!!"))        
        return super(EmployeeUpdateView, self).form_valid(form)
        
    def get_context_date(self):
        return super(EmployeeUpdateView, self).get_context_data()


class EmployeeDetailView(CRUDDetailView):
    model = Employee

    def get_queryset(self):
        return super(EmployeeDetailView, self).get_queryset()
        
    def get_context_date(self):
        return super(EmployeeDetailView, self).get_context_data()
        
class EmployeeListView(CRUDListView):
    model = Employee
    paginate_by = 15

    def get_queryset(self):       
        qs = super(EmployeeListView, self).get_queryset()
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
        return super(EmployeeListView, self).get_context_data()
        
class EmployeeDeleteView(CRUDDeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')
        
    def form_valid(self, form):
        messages.success(self.request, _("Deletion complete!!!"))        
        return super(EmployeeDeleteView, self).form_valid(form)

