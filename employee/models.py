from django.db import models
from organization.models import *
from base.models import BaseModel

class Employee(BaseModel):
    department = models.ForeignKey(Department)
# Create your models here.
