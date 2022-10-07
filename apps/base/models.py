from tabnanny import verbose
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    BaseModel
    """
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado',default=True)
    create_date = models.DateTimeField('Fecha de creación',auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField('Fecha de actualización',auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField('Fecha de eliminación',auto_now_add=False, auto_now=True, null=True, blank=True)    

    class Meta:        
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'