from django.contrib import admin
from .models import Pet, Vaccine, Category

# Register your models here.

#admin.site.register(PetLost)
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','city', 'user', 'description', 'active', 'photo', 'category_name',]
    search_fields = ['id', 'name']

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'description']
    search_fields = ['id', 'name']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

