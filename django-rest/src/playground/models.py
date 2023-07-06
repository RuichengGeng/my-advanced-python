from django.db import models

# Create your models here.
from django.db import models


# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

