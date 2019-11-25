from django.db import models

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()

    
    class Meta:
        verbose_name = 'Vaccine'
        verbose_name_plural = 'Vaccines'

    def __str__(self):
        return self.name

