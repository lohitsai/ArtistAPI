from django.db import models

work_choices = (("Youtube", "Youtube"), ("Instagram", "Instagram"), ("Other", "Other"))


# Create your models here.
class WorkModel(models.Model):
    link = models.CharField(max_length=150)
    workType = models.CharField(choices=work_choices, max_length=10)

    def __str__(self):
        return "Work id: " + str(self.id)
