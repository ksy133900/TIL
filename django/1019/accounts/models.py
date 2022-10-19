from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
