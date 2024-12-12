from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
class CustomModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view_custom", "Can view custom"),
            ("can_edit_custom", "Can edit custom"),
        ]
