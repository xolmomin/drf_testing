from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, ForeignKey


class User(AbstractUser):
    phone = CharField(max_length=9, null=True, blank=True)  # 901001010
    is_verified_phone = BooleanField(default=False)
