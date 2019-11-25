from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PetList, PetDestroy, PetCreate, PetUpdate, PetGet, CategoryList, VaccineList

urlpatterns = [
    path('pets/', PetList.as_view()),
    path('pets/edit/<pk>/', PetUpdate.as_view()),
    path('pets/add/', PetCreate.as_view()),
    path('pets/<pk>/', PetDestroy.as_view()),
    path('pets/get/<pk>', PetGet.as_view()),
    path('categories/', CategoryList.as_view()),
    path('vaccines/', VaccineList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)