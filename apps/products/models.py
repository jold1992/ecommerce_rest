from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):

    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Unidad de medida")
        verbose_name_plural = ("Unidades de medida")

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField('Descripción', max_length=50, blank=False, null=False)
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Cateogría de producto")
        verbose_name_plural = ("Catégorías de producto")

    def __str__(self):
        return self.description

class Indicator(BaseModel):
    """Model definition for Indicator."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta', blank=True, null=True)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de oferta'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de producto', blank=False, null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de producto')
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
