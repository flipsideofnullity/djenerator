from djenerator.models import *

class BaseModel(CRUDBase, CRUDURLMixin):
    """
    Provides the base class for the rest of the models! Also to be included is
    the manager.
    """
    class Meta:
        abstract = True
