from django.db import models
from Work.models import WorkModel
from django.contrib.auth import get_user_model


# Create your models here.
class ArtistModel(models.Model):
    name = models.CharField(max_length=30)
    userInstance = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    work = models.ManyToManyField(WorkModel)

    def __str__(self):
        return self.name
