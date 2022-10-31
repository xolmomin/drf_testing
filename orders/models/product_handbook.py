from django.db.models import SmallIntegerField, ForeignKey, SET_NULL
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import BaseModel
from shared.django.models import SlugModel, UserProductModel


class Tag(SlugModel):
    pass


class Category(MPTTModel, SlugModel):
    parent = TreeForeignKey('self', SET_NULL, 'children', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Cart(BaseModel):
    quantity = SmallIntegerField(default=1)


class Wishlist(UserProductModel):
    pass
