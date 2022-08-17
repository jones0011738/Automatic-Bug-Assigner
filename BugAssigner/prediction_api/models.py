from django.db import models
from django.conf import settings
# Create your models here.
class Request(models.Model):
    request_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="request_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Result(models.Model):
    request = models.ForeignKey(Request, related_name="request_results",
            on_delete=models.CASCADE)
    result = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.request.title
