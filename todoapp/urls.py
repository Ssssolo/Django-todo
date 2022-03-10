from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, adaugare, editare, sterge, clonare, prioritate, completare


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('adaugare/', adaugare, name="adaugare"),
    path('editare/<int:id>', editare, name="editare"),
    path('clonare/<int:id>', clonare, name="clonare"),
    path('prioritate/<int:id>', prioritate, name="prioritate"),
    path('completare/<int:id>', completare, name="completare"),
    path('sterge/<int:id>', sterge, name="sterge")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
