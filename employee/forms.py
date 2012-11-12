from django import forms

from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = [
            "created_at", "modified_at", "created_by", 
            "modified_by", "is_deleted", "is_active", "version",
        ]

