from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('curso/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]