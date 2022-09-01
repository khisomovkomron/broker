from django.db import models
import uuid


class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    total_shares = models.IntegerField()
    price = models.FloatField(max_length=255)
    
    def __str__(self):
        return self.title