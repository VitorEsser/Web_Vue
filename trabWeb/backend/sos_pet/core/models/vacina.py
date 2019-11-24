from django.db import models
from django.contrib.auth.models import User

class Vaccine(models.Model):
	name = models.TextField()
    amount = models.PositiveIntegerField()
    kind = models.TextField()
	description = models.TextField()
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'vaccine'