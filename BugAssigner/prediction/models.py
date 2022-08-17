from django.db import models


# Create your models here.
class Prediction(models.Model):
  title = models.CharField(max_length=200, db_index=True)
  description = models.TextField()

  def __str__(self):
    return f'Prediction {self.id}'
