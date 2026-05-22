from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class likedItem(models.Model):
    # inventory=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
#object
# type
#  id
content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
content_object=GenericForeignKey()
object_id=models.PositiveIntegerField()