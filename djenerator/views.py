from django.views.generic import *
from django.contrib.auth.decorators import *

class RestrictedListView(ListView):
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        @login_required        
        def wrapper(request, *args, **kwargs):
            return super(RestrictedListView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):    
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        @login_required        
        def wrapper(request, *args, **kwargs):
            return super(RestrictedUpdateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedCreateView(CreateView):
    def dispatch(self, request, *args, **kwargs):    
        @permission_required('%s.create_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        @login_required        
        def wrapper(request, *args, **kwargs):
            return super(RestrictedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class RestrictedDeleteView(DeleteView):
    def dispatch(self, request, *args, **kwargs):    
        @permission_required('%s.delete_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        @login_required        
        def wrapper(request, *args, **kwargs):
            return super(RestrictedDeleteView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)
        
class RestrictedDetailView(DetailView):
    def dispatch(self, request, *args, **kwargs):
        #@permission_required('%s.view_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        @login_required
        def wrapper(request, *args, **kwargs):
            return super(RestrictedDetailView, self).dispatch(request, *args, **kwargs)            
        return wrapper(request, *args, **kwargs)

class CRUDListView(RestrictedListView): pass
class CRUDCreateView(RestrictedCreateView): pass
class CRUDUpdateView(RestrictedUpdateView): pass
class CRUDDeleteView(RestrictedDeleteView): pass
class CRUDDetailView(RestrictedDetailView): pass
