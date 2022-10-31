from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from orders.models import Category, Product, Wishlist, ProductImage, Cart, Comment, Tag


class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    exclude = ('slug',)
    mptt_level_indent = 20


admin.site.register(Category, CategoryMPTTModelAdmin)


#
# @admin.register(Category)
# class CategoryAdmin(MPTTModelAdmin):
#     exclude = ('slug',)


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    exclude = ('slug',)


# class TagTabularInline(TabularInline):


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass
    # inlines = TagTabularInline
