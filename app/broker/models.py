from django.db import models
import uuid


class Shares(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    total_shares = models.IntegerField()
    price = models.FloatField(max_length=250)
    
    def __str__(self):
        return self.title

# Create your models here.
class Broker(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title


