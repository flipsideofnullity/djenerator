from django import forms

from .models import *

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = [
            "created_at", "modified_at", "created_by", 
            "modified_by", "is_deleted", "is_active", "version",
        ]

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = [
            "created_at", "modified_at", "created_by", 
            "modified_by", "is_deleted", "is_active", "version",
        ]

