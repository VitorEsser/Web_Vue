from django.db import models
from django.db.models.fields import DateTimeField

from .vaccine import Vaccine
from .category import Category


class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='pet', blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        related_name='pets',
        on_delete = models.CASCADE,
    )
    vaccines = models.ManyToManyField(
        'Vaccine',
        related_name='pets',
        through='PetVaccine'
    )
    
    def __str__(self):
        return self.name

    @property
    def category_name(self):
        return self.category.name

class PetVaccine(models.Model):
    pet = models.ForeignKey(
        'Pet',
        on_delete = models.CASCADE,
    )
    vaccine = models.ForeignKey(
        'Vaccine',
        on_delete = models.CASCADE,
    )
    date_vaccine = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str((self.pet, self.vaccine))

    class Meta:
        verbose_name = 'PetVaccine'
        verbose_name_plural = 'PetVaccines'