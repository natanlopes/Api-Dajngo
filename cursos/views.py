from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """ api de cursos
    """
    def get(request):
        cursos = Curso.objects.all()
        serilizer = CursoSerializer(cursos, many=True)
        return Response(serilizer.data)


class AvaliacaoAPIView(APIView):
    """ api de avaliacao
    """

    def get(request):
        avaliacoes = Avaliacao.objects.all()
        serilizer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serilizer.data)
