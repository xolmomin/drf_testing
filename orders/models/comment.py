from django.db.models import CharField, ForeignKey, CASCADE, SmallIntegerField

from shared.django import BaseModel


class Comment(BaseModel):
    user = ForeignKey('users.User', CASCADE)
    product = ForeignKey('orders.Product', CASCADE)
    parent = ForeignKey('self', CASCADE, null=True, blank=True)
    text = CharField(max_length=255)
    rate = SmallIntegerField(default=0)
