from django.db import transaction
from rest_framework import serializers
from core.models import Pet, Category, Vaccine, PetVaccine

class PetSerializer(serializers.ModelSerializer):
    vaccines = serializers.StringRelatedField(many=True)
    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'email', 'phone',
            'description', 'photo', 'created', 'active',
            'category', 'category_name', 'vaccines',
        )

    
class PetCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'email', 'phone',
            'description', 'photo', 'created', 'active',
            'category', 'category_name', 'vaccines',
        )

    @transaction.atomic
    def create(self, validated_data):
        pet = Pet.objects.create(**validated_data)
        if "vaccines" in self.initial_data:
            vaccines = self.initial_data.get("vaccines")
            for vaccine in vaccines:
                vaccine_id = vaccine.get("vaccine")
                print(vaccine_id)
                vaccine_instance = Vaccine.objects.get(pk=vaccine_id)
                print(vaccine_instance)
                PetVaccine(pet=pet, vaccine=vaccine_instance).save()
        pet.save()
        return pet

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name'
        )

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = (
            'id', 'name', 'description'
        )