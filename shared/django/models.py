from django.db.models import Model, DateTimeField, CharField, SlugField, ForeignKey, CASCADE, SET_NULL
from django.utils.text import slugify


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateModel(Model):
    updated_by = ForeignKey('users.User', CASCADE, 'products')
    created_by = ForeignKey('users.User', SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class UserProductModel(BaseModel):
    user = ForeignKey('users.User', CASCADE)
    product = ForeignKey('orders.Product', CASCADE)

    class Meta:
        abstract = True


class SlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        print(123)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
