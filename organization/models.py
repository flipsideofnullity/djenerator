from django.db import models
from base.models import BaseModel

class Organization(BaseModel):
    organization_name = models.CharField(max_length=63, blank=True)
    address = models.TextField(blank=True)

class Department(BaseModel):
    organization = models.ForeignKey(Organization,)
# Create your models here.
