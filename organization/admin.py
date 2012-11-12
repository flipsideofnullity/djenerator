from django.contrib import admin

from .models import *
from .forms import *

class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentForm
    list_display = ["__unicode__", "created_by", "modified_by", "created_at", "modified_at",]
    date_hierarchy = "created_at"
    list_filter = ["created_at", "modified_at"]
    search_fields = ["remarks"]
        
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.version += 1
        obj.modified_by = request.user
        obj.save()
        return super(DepartmentAdmin, self).save_model(
            request, obj, form, change)

admin.site.register(Department, DepartmentAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationForm
    list_display = ["__unicode__", "created_by", "modified_by", "created_at", "modified_at",]
    date_hierarchy = "created_at"
    list_filter = ["created_at", "modified_at"]
    search_fields = ["remarks"]
        
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.version += 1
        obj.modified_by = request.user
        obj.save()
        return super(OrganizationAdmin, self).save_model(
            request, obj, form, change)

admin.site.register(Organization, OrganizationAdmin)

