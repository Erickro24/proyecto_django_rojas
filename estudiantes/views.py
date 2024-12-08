from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Estudiante, Curso, Inscripcion, Profesor
from .serializers import EstudianteSerializer, CursoSerializer, InscripcionSerializer, ProfesorSerializer

# ModelViewSets
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    
class CustomAPI(APIView):
    def get(self, request):
        return Response({"message": "Hola desde Custom API"})