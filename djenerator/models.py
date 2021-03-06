from django.db import models

from django.contrib.auth.models import User
from django.db import models

class CRUDBase(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, 
        related_name="%(app_label)s_%(class)s_created")
    modified_by = models.ForeignKey(User, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_updated")
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    version = models.IntegerField(default=0)
    remarks = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return "{}".format(self.name)
        
class CRUDURLMixin(object):
    def get_identifier(self):
        return self.pk

    @models.permalink
    def get_absolute_url(self):
        name = "".join(self._meta.verbose_name_raw.split(" "))
        return ('{}-detail'.format(name), 
                [self.get_identifier()])
                
    @models.permalink
    def get_create_url(self):
        name = "".join(self._meta.verbose_name_raw.split(" "))    
        return ('{}-create'.format(name),)
        
    @models.permalink
    def get_update_url(self):
        name = "".join(self._meta.verbose_name_raw.split(" "))    
        return ('{}-update'.format(name), 
                [self.get_identifier()])
                
    @models.permalink
    def get_delete_url(self):
        name = "".join(self._meta.verbose_name_raw.split(" "))    
        return ('{}-delete'.format(name), 
                [self.get_identifier()])
                
    @models.permalink
    def get_list_url(self):
        name = "".join(self._meta.verbose_name_raw.split(" "))    
        return ('{}-list'.format(name),)
