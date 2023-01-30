from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    APi de curso
    """
    def get(self,request):
        cursos = Curso.objects.all()
        serilizer = CursoSerializer(cursos,many=True)
        return Response(serilizer.data)

class AvaliacaoAPIView(APIView):
    """
    APi de Avaliacao
    """
    def get(self,request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes,many=True)
        return Response(serializer.data)