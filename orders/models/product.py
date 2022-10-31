from ckeditor.fields import RichTextField
from django.db.models import DecimalField, ForeignKey, CASCADE, ImageField, SmallIntegerField, JSONField, \
    ManyToManyField

from shared.django import BaseModel
from shared.django.models import SlugModel, UpdateModel


class Product(SlugModel, UpdateModel, BaseModel):
    price = DecimalField(decimal_places=2, max_digits=25)
    description = RichTextField()
    discount = SmallIntegerField(default=0)
    quantity = SmallIntegerField(default=0)
    shipping_cost = DecimalField(decimal_places=2, max_digits=12)
    spec = JSONField(default=dict)
    tags = ManyToManyField('orders.Tag')
    category = ForeignKey('orders.Category', CASCADE)

    @property
    def is_in_stock(self):
        return self.quantity > 0


class ProductImage(BaseModel):
    product = ForeignKey('orders.Product', CASCADE)
    picture = ImageField(upload_to='products/images/y/m/d')
